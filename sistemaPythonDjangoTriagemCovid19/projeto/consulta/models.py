from __future__ import unicode_literals

from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.gerador_hash import gerar_hash
    
class Consulta(models.Model): 
    
    medico = models.ForeignKey('usuario.Usuario', verbose_name= 'Médico na consulta *', on_delete=models.PROTECT, related_name='medico')
    unidade = models.ForeignKey('unidade.Unidade', verbose_name= 'Unidade de Atendimento *', on_delete=models.PROTECT, related_name='unidade_consulta')

    data = models.DateField('Data da consulta ', max_length=10, help_text='Use dd/mm/aaaa')
    hora = models.TimeField('Hora da consulta ', max_length=10, help_text='Use hh:mm')
    # paciente = models.CharField('Informe o nome completo do paciente *', max_length=100, help_text= '* indica campos obrigatórios')
    
    paciente_triagem = models.ForeignKey('triagem.Triagem', blank=False, null=True, verbose_name= 'Paciente vindo da triagem *', on_delete=models.PROTECT, related_name='paciente_triagem')

    prescricao = models.TextField('Prescrição *', max_length=1000, help_text= '* indica campos obrigatórios')
    medicamentos = models.ManyToManyField('medicamento.Medicamento', verbose_name='Medicamento(s)', null=True, blank=True, related_name='medicamento', help_text='Para selecionar ou deselecionar um medicamento pressione CTRL + Botão Esquerdo do mouse ou Command + Botão Esquerdo do mouse')
    
    slug = models.SlugField('Hash',max_length= 200, null=True, blank=True)
    
    objects = models.Manager()
    
    class Meta:
        ordering            =   ['-data', '-hora', 'paciente_triagem__paciente2__nome']
        verbose_name        =   ('consulta')
        verbose_name_plural =   ('consultas')
        unique_together     =   [['data','hora','paciente_triagem']]

    def __str__(self):
        return "Paciente: %s. Médico: %s. Data: %s. Hora: %s." % (self.paciente, self.medico, self.data, self.hora)

    def save(self, *args, **kwargs):
        
        
        self.data = datetime.now()
        self.hora = datetime.now()
        
        if not self.slug:
            self.slug = gerar_hash()
        super(Consulta, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('consulta_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('consulta_delete', args=[str(self.id)]) 
    
    