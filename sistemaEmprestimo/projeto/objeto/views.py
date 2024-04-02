from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse

from utils.decorators import LoginRequiredMixin,  StaffRequiredMixin

from .models import Objeto


class ObjetoListView(LoginRequiredMixin, ListView):
    model = Objeto


class ObjetoCreateView(LoginRequiredMixin,  StaffRequiredMixin, CreateView):
    model = Objeto
    fields = ['codigo', 'tipo', 'descricao', 'valor', 'arquivo_foto']
    success_url = 'objeto_list'
    
    def form_valid(self, form):
        limite_mb = 3 * 1024 * 1024
        obj = form.instance
        
        if (not obj.arquivo_foto or (obj.arquivo_foto and obj.arquivo_foto.file.size <= limite_mb)):
            form.save()
            return super(ObjetoCreateView, self).form_valid(form)
        else:
            messages.danger(self.request, 'Sistema somente suporta 3 Mb na foto!')
            return super(ObjetoCreateView, self).form_invalid(form)
    
    def get_success_url(self):
        messages.success(self.request, 'Objeto pessoal cadastrado com sucesso na plataforma!')
        return reverse(self.success_url)


class ObjetoUpdateView(LoginRequiredMixin,  StaffRequiredMixin, UpdateView):
    model = Objeto
    fields = ['codigo', 'tipo', 'descricao', 'valor', 'arquivo_foto']
    success_url = 'objeto_list'
    
    def form_valid(self, form):
        limite_mb = 3 * 1024 * 1024
        obj = form.instance
        
        if (not obj.arquivo_foto or (obj.arquivo_foto and obj.arquivo_foto.file.size <= limite_mb)):
            form.save()
            return super(ObjetoUpdateView, self).form_valid(form)
        else:
            messages.danger(self.request, 'Sistema somente suporta 3 Mb na foto!')
            return super(ObjetoUpdateView, self).form_invalid(form)
    
    def get_success_url(self):
        messages.success(self.request, 'Dados do objeto pessoal atualizados com sucesso na plataforma!')
        return reverse(self.success_url)


class ObjetoDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Objeto
    success_url = 'objeto_list'

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
            messages.error(request, 'Há dependências ligadas a esse objeto, permissão negada!')
        return redirect(self.success_url)