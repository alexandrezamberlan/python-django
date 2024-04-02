from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse

from utils.decorators import LoginRequiredMixin,  StaffRequiredMixin

from .models import Emprestimo
from .forms import EmprestimoForm


class EmprestimoListView(LoginRequiredMixin,  ListView):
    model = Emprestimo


class EmprestimoCreateView(LoginRequiredMixin,  StaffRequiredMixin, CreateView):
    model = Emprestimo
    form_class = EmprestimoForm
    success_url = 'emprestimo_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Empréstimo cadastrado com sucesso na plataforma!')
        return reverse(self.success_url)


class EmprestimoUpdateView(LoginRequiredMixin,  StaffRequiredMixin, UpdateView):
    model = Emprestimo
    form_class = EmprestimoForm
    success_url = 'emprestimo_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Dados do empréstimo atualizados com sucesso na plataforma!')
        return reverse(self.success_url)


class EmprestimoDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Emprestimo
    success_url = 'emprestimo_list'

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
            messages.error(request, 'Há dependências ligadas a esse empréstimo, permissão negada!')
        return redirect(self.success_url)