from __future__ import unicode_literals

from django.contrib import messages

from django.db.models import Q

from django.shortcuts import redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin

from .models import Evento

from .forms import BuscaEventoForm, EventoForm


class EventoListView(LoginRequiredMixin, ListView):
    model = Evento

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dados filtrando
            context['form'] = BuscaEventoForm(data=self.request.GET)
        else:
            #quando acessa sem dados filtrando
            context['form'] = BuscaEventoForm()
        return context

    def get_queryset(self):                
        qs = super().get_queryset().all()        
        
        if self.request.GET:
            #quando ja tem dados filtrando
            form = BuscaEventoForm(data=self.request.GET)
        else:
            #quando acessa sem dados filtrando
            form = BuscaEventoForm()

        if form.is_valid():            
            pesquisa = form.cleaned_data.get('pesquisa')            
                        
            if pesquisa:
                qs = qs.filter(nome__icontains=pesquisa)
            
        return qs
 

class EventoCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Evento
    # fields = ['nome', 'tipo', 'instituicao', 'coordenador', 'coordenador_suplente', 'data_inicio', 'data_limite_trabalhos', 'modelo_artigo', 'arquivo_modelo', 'is_active']
    form_class = EventoForm
    success_url = 'evento_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Evento cadastrado com sucesso na plataforma!')
        return reverse(self.success_url)


class EventoUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Evento
    # fields = ['nome', 'tipo', 'instituicao', 'coordenador', 'coordenador_suplente', 'data_inicio', 'data_limite_trabalhos', 'modelo_artigo', 'arquivo_modelo', 'is_active']
    form_class = EventoForm
    success_url = 'evento_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Evento atualizado com sucesso na plataforma!')
        return reverse(self.success_url) 


class EventoDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Evento
    success_url = 'evento_list'

    def get_success_url(self):
        messages.success(self.request, 'Evento removido com sucesso da plataforma!')
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
            messages.error(request, 'Há dependências ligadas à esse Evento, permissão negada!')
        return redirect(self.success_url)