from __future__ import unicode_literals

from django.contrib import messages

from django.db.models import Q

from django.shortcuts import redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin

from .models import TipoEvento

from .forms import BuscaTipoEventoForm


class TipoEventoListView(LoginRequiredMixin, ListView):
    model = TipoEvento

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dados filtrando
            context['form'] = BuscaTipoEventoForm(data=self.request.GET)
        else:
            #quando acessa sem dados filtrando
            context['form'] = BuscaTipoEventoForm()
        return context

    def get_queryset(self):                
        qs = super().get_queryset().all()        
        
        if self.request.GET:
            #quando ja tem dados filtrando
            form = BuscaTipoEventoForm(data=self.request.GET)
        else:
            #quando acessa sem dados filtrando
            form = BuscaTipoEventoForm()

        if form.is_valid():            
            pesquisa = form.cleaned_data.get('pesquisa')            
                        
            if pesquisa:
                qs = qs.filter(descricao__icontains=pesquisa)            
            
        return qs
 

class TipoEventoCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = TipoEvento
    fields = ['descricao', 'is_active']
    success_url = 'tipo_evento_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Tipo de evento cadastrado com sucesso na plataforma!')
        return reverse(self.success_url)


class TipoEventoUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = TipoEvento
    fields = ['descricao', 'is_active']
    success_url = 'tipo_evento_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Tipo de evento atualizado com sucesso na plataforma!')
        return reverse(self.success_url) 
    
    
class TipoEventoDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = TipoEvento
    success_url = 'tipo_evento_list'

    def get_success_url(self):
        messages.success(self.request, 'Tipo de evento removido com sucesso na plataforma!')
        return reverse(self.success_url) 

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à esse tipo de evento, permissão negada!')
        return redirect(self.success_url)