from __future__ import unicode_literals

from datetime import datetime
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.gerador_hash import gerar_hash

class PacienteAtivoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Paciente(models.Model):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    SEXO = (
        ('FEMININO', 'Feminino'),
        ('MASCULINO', 'Masculino' ),
    )
    
    nome = models.CharField('Nome completo *', max_length=200, help_text='* Campo obrigatório')
    cpf = models.CharField('CPF *', max_length=11, help_text='* Somente os números', unique=True)
    email = models.EmailField('Email do paciente ou do responsável *', max_length=200)
    #sexo, dataNascimento
    sexo = models.CharField('Sexo *', max_length=10, choices=SEXO, blank=False, null=True, help_text='* Campos obrigatórios')
    data_nascimento = models.DateField('Data de nascimento *', blank=False, null=True, max_length=10, help_text='Use dd/mm/aaaa')

    is_active = models.BooleanField('Ativo', default=False, help_text='Se ativo, o paciente pode realizar triagens e consultas')
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)

    objects = models.Manager()
    pacientes_ativos = PacienteAtivoManager()

    
    class Meta:
        ordering            =   ['-is_active','nome']
        verbose_name        =   'paciente'
        verbose_name_plural =   'pacientes'

    def __str__(self):
        return '%s - %s - %s' % (self.nome, self.sexo, self.idade)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        self.nome = self.nome.upper()
        self.email = self.email.lower()
        super(Paciente, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('paciente_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('paciente_delete', args=[str(self.id)])


    @property
    def idade(self):
        try:
            return  datetime.now().year - self.data_nascimento.year
        except:
            return 0