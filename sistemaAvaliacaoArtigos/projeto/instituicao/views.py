from __future__ import unicode_literals

from django.contrib import messages

from django.shortcuts import redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin

from .models import Instituicao


class InstituicaoListView(LoginRequiredMixin, ListView):
    model = Instituicao
 

class InstituicaoCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Instituicao
    fields = ['nome', 'sigla', 'pais', 'estado', 'cidade', 'is_active']
    success_url = 'instituicao_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Instituição cadastrada com sucesso na plataforma!')
        return reverse(self.success_url)


class InstituicaoUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Instituicao
    fields = ['nome', 'sigla', 'pais', 'estado', 'cidade', 'is_active']
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
            messages.error(request, 'Há dependências ligadas à essa Instituição, permissão negada!')
        return redirect(self.success_url)