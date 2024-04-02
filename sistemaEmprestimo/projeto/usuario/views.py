from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse

from django.views.generic import ListView, TemplateView, DetailView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from mail_templated import EmailMessage

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin

from .models import Usuario
from .forms import UsuarioRegisterForm


class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario


class UsuarioCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Usuario
    fields = ['tipo', 'nome', 'apelido', 'email', 'celular', 'password', 'is_active']
    success_url = 'usuario_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Usuário cadastrado com sucesso na plataforma!')
        return reverse(self.success_url)


class UsuarioUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Usuario
    fields = ['tipo', 'nome', 'apelido', 'email', 'celular', 'is_active']
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


class UsuarioRegisterView(CreateView):
    model = Usuario
    form_class = UsuarioRegisterForm
    template_name = 'usuario/usuario_register_form.html'

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.save()
    #     return super(UsuarioRegisterView, self).form_valid(form)
    
    def get_success_url(self):
        message = EmailMessage('usuario/email/validacao_email.html', {'usuario': self.object},
                               settings.EMAIL_HOST_USER, to=[self.object.email])
        message.send()     
        return reverse('usuario_register_success')


class UsuarioRegisterSuccessView(TemplateView):
    template_name= 'usuario/usuario_register_success.html'


class UsuarioRegisterActivateView(RedirectView):
    models = Usuario

    def get_redirect_url(self, *args, **kwargs):
        self.object = Usuario.objects.get(slug=kwargs.get('slug'))
        self.object.is_active = True
        self.object.save()
        login(self.request, self.object)
        messages.success(self.request, 'Obrigado por acessar o TFG ONLINE. Esta é a sua área restrita de acompanhamento de TFG.')
        return reverse('home')