from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager
from django.db import models
from django.db.models import Q
from django.urls import reverse
#from django.utils.translation import ugettext_lazy as _

from datetime import timedelta, datetime

from utils.gerador_hash import gerar_hash


class AdministradorAtivoManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(tipo='ADMINISTRADOR', is_active=True)


class CoordenadorAtivoManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(Q(tipo='COORDENADOR') | Q(tipo='ADMINISTRADOR'), is_active=True)
    
class MembroAtivoManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(tipo='MEMBRO', is_active=True)


class Usuario(AbstractBaseUser):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TIPOS_USUARIOS = (
        ('ADMINISTRADOR', 'Administrador'),
        ('COORDENADOR', 'Coordenador de Evento' ),
        ('MEMBRO', 'Membro' ),        
    )
    #(técnico, graduando, graduado, especialista, mestre, doutor)
    TITULACAO = (
        ('TECNICO', 'Técnico'),
        ('GRADUANDO', 'Graduando' ),
        ('GRADUADO', 'Graduado' ),        
        ('ESPECIALISTA', 'Especialista'),
        ('MESTRE', 'Mestre' ),
        ('DOUTOR', 'Doutor' ),        
    )

    #(Ciências Humana, Ciências da Saúde, Ciências Sociais, Ciências Tecnológicas)
    AREA = (
        ('HUMANAS', 'Ciências Humanas'),
        ('SAUDE', 'Ciências da Saúde' ),
        ('SOCIAIS', 'Ciências Sociais' ),        
        ('TECNOLOGICA', 'Ciências Tecnológicas'),        
    )

    USERNAME_FIELD = 'email'

    tipo = models.CharField('Tipo do usuário *', max_length=15, choices=TIPOS_USUARIOS, default='MEMBRO', help_text='* Campos obrigatórios')
    nome = models.CharField('Nome completo *', max_length=100)
    titulacao = models.CharField('Titulação', max_length=15, choices=TITULACAO, null=True, blank=True, help_text='Selecione a maior titulação')
    area = models.CharField('Área de pesquisa do usuário *', max_length=11, choices=AREA, help_text='Escolha área de interesse de trabalho')
    instituicao = models.CharField('Instituição a que pertence *', max_length=50, help_text='Registre a instituição, ou universidade, ou empresa')
    email = models.EmailField('Email', unique=True, max_length=100, db_index=True)
    celular = models.CharField('Número celular com DDD *', max_length=11, help_text="Use DDD, por exemplo 55987619832")
    cpf = models.CharField('CPF *', max_length=14, help_text='ATENÇÃO: Somente os NÚMEROS')    
    
    is_active = models.BooleanField('Ativo', default=False, help_text='Se ativo, o usuário tem permissão para acessar o sistema')
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)

    objects = UserManager()
    administradores = AdministradorAtivoManager()
    coordenadores = CoordenadorAtivoManager()
    membros = MembroAtivoManager()

    class Meta:
        ordering            =   ['-tipo','nome']
        verbose_name        =   ('usuário')
        verbose_name_plural =   ('usuários')

    def __str__(self):
        return '%s - %s' % (self.nome, self.email)

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
        self.instituicao = self.instituicao.upper()
        self.email = self.email.lower()
        if not self.id:
            self.set_password(self.password) #criptografa a senha digitada no forms
        super(Usuario, self).save(*args, **kwargs)

    def get_id(self):
        return self.id

    @property
    def get_primeiro_nome(self):
        lista = self.nome.split(" ")
        return lista[0]

    @property
    def is_staff(self):
        if self.tipo == 'ADMINISTRADOR':
            return True
        return False

    @property
    def get_absolute_url(self):
        return reverse('usuario_update', kwargs={'slug': self.slug})

    @property
    def get_delete_url(self):
        return reverse('usuario_delete', kwargs={'slug': self.slug})

    @property
    def get_usuario_register_activate_url(self):
        return '%s%s' % (settings.DOMINIO_URL, reverse('usuario_register_activate', kwargs={'slug': self.slug}))
