from __future__ import unicode_literals

from django.contrib import messages

from django.shortcuts import redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin, EnfermeiroRequiredMixin

from .models import Medicamento

from .forms import BuscaMedicamentoForm


class MedicamentoListView(LoginRequiredMixin, ListView):
    model = Medicamento

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dados filtrando
            context['form'] = BuscaMedicamentoForm(data=self.request.GET)
        else:
            #quando acessa sem dados filtrando
            context['form'] = BuscaMedicamentoForm()
        return context

    def get_queryset(self):                
        qs = super().get_queryset().all()
        
        if self.request.GET:
            #quando ja tem dados filtrando
            form = BuscaMedicamentoForm(data=self.request.GET)
        else:
            #quando acessa sem dados filtrando
            form = BuscaMedicamentoForm()

        if form.is_valid():            
            tarja = form.cleaned_data.get('tarja')
            tipo = form.cleaned_data.get('tipo')
                        
            if tarja:
                qs = qs.filter(tarja=tarja)

            if tipo:
                qs = qs.filter(tipo=tipo)
            
        return qs
 

class MedicamentoCreateView(LoginRequiredMixin, EnfermeiroRequiredMixin, CreateView):
    model = Medicamento
    fields = ['nome_real', 'nome_fantasia', 'tarja', 'tipo', 'quantidade', 'fornecedor' ,'is_active']
    success_url = 'medicamento_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Medicamento cadastrado com sucesso na plataforma!')
        return reverse(self.success_url)


class MedicamentoUpdateView(LoginRequiredMixin, EnfermeiroRequiredMixin, UpdateView):
    model = Medicamento
    fields = ['nome_real', 'nome_fantasia', 'tarja', 'tipo', 'quantidade', 'fornecedor', 'is_active']
    success_url = 'medicamento_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Medicamento atualizado com sucesso na plataforma!')
        return reverse(self.success_url) 


class MedicamentoDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Medicamento
    success_url = 'medicamento_list'

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
            messages.error(request, 'Há dependências ligadas à esse Medicamento, permissão negada!')
        return redirect(self.success_url)