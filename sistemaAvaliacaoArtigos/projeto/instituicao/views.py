from __future__ import unicode_literals

from django.contrib import messages

from django.shortcuts import redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin

from .models import Instituicao

from .forms import BuscaInstituicaoForm

class InstituicaoListView(LoginRequiredMixin, ListView):
    model = Instituicao

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dados filtrando
            context['form'] = BuscaInstituicaoForm(data=self.request.GET)
        else:
            #quando acessa sem dados filtrando
            context['form'] = BuscaInstituicaoForm()
        return context

    def get_queryset(self):                
        qs = super().get_queryset().all()
        
        if self.request.GET:
            #quando ja tem dados filtrando
            form = BuscaInstituicaoForm(data=self.request.GET)
        else:
            #quando acessa sem dados filtrando
            form = BuscaInstituicaoForm()

        if form.is_valid():            
            nome  = form.cleaned_data.get('nome')
            sigla = form.cleaned_data.get('sigla')
                        
            if nome:
                qs = qs.filter(tarja=nome)

            if sigla:
                qs = qs.filter(tipo=sigla)
                
        return qs
 

class InstituicaoCreateView(LoginRequiredMixin, CreateView):
    model = Instituicao
    fields = ['nome', 'sigla', 'cidade', 'estado', 'pais','is_active']
    success_url = 'instituicao_list'
    
    def get_success_url(self):
        messages.success(self.request, 'A instituição foi cadastrado com sucesso na plataforma!')
        return reverse(self.success_url)


class InstituicaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Instituicao
    fields = ['nome', 'sigla', 'cidade', 'estado', 'pais','is_active']
    success_url = 'instituicao_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Instituição atualizada com sucesso na plataforma!')
        return reverse(self.success_url) 


class InstituicaoDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Instituicao
    success_url = 'instituicao_list'

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
            messages.error(request, 'Há dependências ligadas à esta instituição, permissão negada!')
        return redirect(self.success_url)