from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login

from django.shortcuts import redirect
from django.urls import reverse

from django.views.generic import ListView, TemplateView, DetailView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from mail_templated import EmailMessage

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin, CoordenadorRequiredMixin

from .models import Usuario
# from .forms import UsuarioRegisterForm


class UsuarioListView(LoginRequiredMixin, CoordenadorRequiredMixin, ListView):
    model = Usuario

    def get_queryset(self):                
        if (not self.request.user.tipo == 'ADMINISTRADOR'):
            qs = super().get_queryset().exclude(tipo = 'ADMINISTRADOR')
        else:
            qs = super().get_queryset().all()
            
        return qs



class UsuarioCreateView(LoginRequiredMixin, CoordenadorRequiredMixin, CreateView):
    model = Usuario
    fields = ['tipo', 'nome', 'titulacao', 'area', 'instituicao', 'celular', 'cpf', 'email', 'password', 'is_active']
    success_url = 'usuario_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Usuário cadastrado com sucesso na plataforma!')
        return reverse(self.success_url)


class UsuarioUpdateView(LoginRequiredMixin, CoordenadorRequiredMixin, UpdateView):
    model = Usuario
    fields = ['tipo', 'nome', 'titulacao', 'area', 'instituicao', 'celular', 'cpf', 'email', 'is_active']
    success_url = 'usuario_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Dados do usuário atualizados com sucesso na plataforma!')
        return reverse(self.success_url)


class UsuarioDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Usuario
    success_url = 'usuario_list'

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
            messages.error(request, 'Há dependências ligadas à esse usuário, permissão negada!')
        return redirect(self.success_url)

