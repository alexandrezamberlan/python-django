from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from datetime import timedelta, datetime

from utils.gerador_hash import gerar_hash


class AdministradorAtivoManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(tipo='ADMINISTRADOR', is_active=True)


class UsuarioAtivoManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(tipo='USUÁRIO', is_active=True) 


class Usuario(AbstractBaseUser):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TIPOS_USUARIOS = (
        ('ADMINISTRADOR', 'Administrador'),
        ('USUÁRIO', 'Usuário' ),
    )

    USERNAME_FIELD = 'email'

    tipo = models.CharField(_('Tipo do usuário *'), max_length=15, choices=TIPOS_USUARIOS, default='USUÁRIO', help_text='* Campos obrigatórios')
    nome = models.CharField(_('Nome completo *'), max_length=100)
    apelido = models.CharField(_('Apelido'), max_length=100, null=True, blank=True)
    email = models.EmailField(_('Email *'), unique=True, max_length=100, db_index=True)
    celular = models.CharField(_('Celular *'),max_length=10, help_text="Com WhattsApp")    
    
    is_active = models.BooleanField(_('Ativo'), default=False, help_text='Se ativo, o usuário tem permissão para acessar o sistema')
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)

    objects = UserManager()
    administradores = AdministradorAtivoManager()
    usuarios = UsuarioAtivoManager()

    class Meta:
        ordering            =   ['apelido', 'nome']
        verbose_name        =   ('usuário')
        verbose_name_plural =   ('usuários')

    def __str__(self):
        return '%s - %s - %s' % (self.apelido, self.nome, self.celular)


    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def get_short_name(self):
        return self.nome[0:15].strip()

    def get_full_name(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        self.nome = self.nome.upper()
        self.apelido = self.apelido.upper()
        if not self.id:
            self.set_password(self.password) #criptografa a senha digitada no forms
        super(Usuario, self).save(*args, **kwargs)

    def get_id(self):
        return self.id

    @property
    def is_staff(self):
        if self.tipo == 'ADMINISTRADOR':
            return True
        return False

    @property
    def get_absolute_url(self):
        return reverse('usuario_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('usuario_delete', args=[str(self.id)])

    @property
    def get_usuario_register_activate_url(self):
        return '%s%s' % (settings.DOMINIO_URL, reverse('usuario_register_activate', kwargs={'slug': self.slug}))
