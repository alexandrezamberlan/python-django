from __future__ import unicode_literals

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import ListView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse

from mail_templated import EmailMessage

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin

from .models import Aviso
from usuario.models import Usuario


class AvisoListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Aviso


class AvisoCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Aviso
    fields = ['titulo', 'texto', 'destinatario', 'enviado', 'is_active']
    success_url = 'aviso_list'
    
    
    def form_valid(self, form):
        aviso = form.save(commit=False)
        
        if (aviso.enviado):
            if aviso.destinatario == 'TODOS':
                destinatarios = Usuario.objects.filter(is_active=True)                
            elif aviso.destinatario == 'COORDENADOR':
                destinatarios = Usuario.objects.filter(is_active=True, tipo='COORDENADOR')
            else:
                destinatarios = Usuario.objects.filter(is_active=True, tipo='MEMBRO')
            
            aviso.save()
        
            try:
                """ enviar e-mail para destinatarios """                
                message = EmailMessage('usuario/email/aviso.html', {'aviso': aviso},
                        settings.EMAIL_HOST_USER, bcc=[usuario.email for usuario in destinatarios])
                
                message.send()
            except Exception as e:
                # alterar para outro tipo de requisição http
                messages.warning(self.request, "Aviso não foi enviado por problemas com servidor! " + str(e))
            
        return super().form_valid(form)
    
    def get_success_url(self):
        messages.success(self.request, 'Aviso cadastrado com sucesso na plataforma!')
        return reverse(self.success_url)


class AvisoUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Aviso
    template_name = 'aviso/aviso_form_update.html'
    fields = ['titulo', 'texto', 'destinatario', 'is_active']
    success_url = 'aviso_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Aviso atualizado com sucesso na plataforma!')
        return reverse(self.success_url) 


class AvisoDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Aviso
    success_url = 'aviso_list'

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
            messages.error(request, 'Há dependências ligadas à esse aviso, permissão negada!')
        return redirect(self.success_url) 
    

class AvisoEnviaEmail(LoginRequiredMixin, StaffRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        
        aviso = Aviso.objects.get(id=kwargs.get('pk'))

        if aviso.destinatario == 'TODOS':
            destinatarios = Usuario.objects.filter(is_active=True)
        elif aviso.destinatario == 'COORDENADOR':
            destinatarios = Usuario.objects.filter(is_active=True, tipo='COORDENADOR')
        else:
            destinatarios = Usuario.objects.filter(is_active=True, tipo='MEMBRO')
    
        try:
            """ enviar e-mail para destinatarios """                
            message = EmailMessage('usuario/email/aviso.html', {'aviso': aviso},
                    settings.EMAIL_HOST_USER, bcc=[usuario.email for usuario in destinatarios])
            
            if message.send():
                messages.success(self.request, 'Aviso reenviado por e-mail com sucesso!')
            else:
                raise Exception()
        except Exception as e:
            # alterar para outro tipo de requisição http
            messages.warning(self.request, "Aviso não foi enviado por problemas com servidor! " + str(e))
        return reverse('aviso_list')


class AvisoListIFrameView(ListView):
    model = Aviso
    context_object_name = 'avisos'
    template_name = 'aviso/avisos.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['avisos'] = Aviso.ativos.filter(destinatario='TODOS')[0:2]
        return context