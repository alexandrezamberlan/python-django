from __future__ import unicode_literals

from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.gerador_hash import gerar_hash
    
class Triagem(models.Model): 
    #dados do responsável
    responsavel = models.ForeignKey('usuario.Usuario', verbose_name= 'Responsável pela triagem *', on_delete=models.PROTECT, related_name='responsavel')
    unidade = models.ForeignKey('unidade.Unidade', verbose_name= 'Unidade de Atendimento *', on_delete=models.PROTECT, related_name='unidade')
    
    #dados do paciente e da consulta
    data = models.DateField(_('Data da triagem '), max_length=10, help_text='Use dd/mm/aaaa')
    hora = models.TimeField(_('Hora da triagem '), max_length=10, help_text='Use hh:mm')
    
    paciente2 = models.ForeignKey('paciente.Paciente', verbose_name= 'Paciente *', null=True, blank=False, on_delete=models.PROTECT, related_name='paciente2')
    
    altura = models.DecimalField(_('Altura em metros *'), max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(2.5)])
    peso = models.DecimalField(_('Peso em kg *'), max_digits=5, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(400.0)])
    
    #dados da triagem
    tem_febre = models.BooleanField(_('Tem febre ?'), default=False)
    tem_dor_cabeca = models.BooleanField(_('Tem dor de cabeça ?'), default=False)
    tem_secrecao_espirros = models.BooleanField(_('Tem secreção nasal ou espirros ?'), default=False)
    tem_irritacao_garganta = models.BooleanField(_('Tem irritação de garganta ?'), default=False)
    tem_tosse = models.BooleanField(_('Tem tosse seca ?'), default=False)
    tem_dificuldade_respiratoria = models.BooleanField(_('Tem dificuldade respiratória ?'), default=False)
    tem_dores_corpo = models.BooleanField(_('Tem dores no corpo ?'), default=False)
    tem_diarreia = models.BooleanField(_('Tem diarréia ?'), default=False)
    viajou = models.BooleanField(_('Viajou nos últimos 14 dias para algum local com casos confirmados de COVID 19 ?'), default=False)
    contatou = models.BooleanField(_('Esteve em contato no últimos 14 dias com alguém com quadro diagnosticado de COVID 19 ?'), default=False)

    slug = models.SlugField('Hash',max_length= 200, null=True, blank=True)
    
    objects = models.Manager()
    
    class Meta:
        ordering            =   ['-data', '-hora', 'paciente2__nome']
        verbose_name        =   ('triagem')
        verbose_name_plural =   ('triagens')
        unique_together     =   [['data','hora','paciente2']]

    def __str__(self):
        return "Paciente: %s. Resultado: %s. Data: %s. Hora: %s" % (self.paciente2, self.resultado_literal_triagem, self.data, self.hora)

    def save(self, *args, **kwargs):
        self.data = datetime.now()
        self.hora = datetime.now()
        
        if not self.slug:
            self.slug = gerar_hash()

        

        super(Triagem, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('triagem_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('triagem_delete', args=[str(self.id)]) 
    
    @property
    def imc(self):
        return self.peso/(self.altura * self.altura)
    
    @property
    def resultado_numerico_triagem(self):
        soma = 0
        if self.tem_febre:
            soma = soma + 5
        if self.tem_dor_cabeca:
            soma = soma + 1
        if self.tem_secrecao_espirros:
            soma = soma + 1
        if self.tem_irritacao_garganta:
            soma = soma + 1
        if self.tem_tosse:
            soma = soma + 3
        if self.tem_dificuldade_respiratoria:
            soma = soma + 10
        if self.tem_dores_corpo:
            soma = soma + 1
        if self.tem_diarreia:
            soma = soma + 1
        if self.viajou:
            soma = soma + 3
        if self.contatou:
            soma = soma + 10
        
        return soma    
    
    @property
    def resultado_literal_triagem(self):
        if self.resultado_numerico_triagem <= 9:
            return 'Risco Baixo'
        if self.resultado_numerico_triagem <= 19:
            return 'Risco Médio'
        else:
            return 'Risco Alto'