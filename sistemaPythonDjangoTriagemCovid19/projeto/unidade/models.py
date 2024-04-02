from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.gerador_hash import gerar_hash


class Unidade(models.Model):
    
    nome = models.CharField(_('Nome da Unidade de Atendimento *'), unique=True, max_length=100, help_text='* Campos obrigatórios')
    endereco = models.CharField(_('Rua, número, complemento, bairro e CEP *'), max_length=150)
    fone = models.CharField(_('Telefone de contato *'), max_length=12) 
    coordenador = models.ForeignKey('usuario.Usuario', verbose_name= 'Coordenador da Unidade de Atendimento *', on_delete=models.PROTECT, related_name='coordenador')
    is_active = models.BooleanField(_('Ativo'), default=True, help_text='Se ativo, o curso pode ser usado no sistema')
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)

    objects = models.Manager()

    
    class Meta:
        ordering            =   [u'nome']
        verbose_name        =   _(u'unidade')
        verbose_name_plural =   _(u'unidadess')

    def __str__(self):
        return '%s - %s' % (self.nome, self.coordenador)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        self.nome = self.nome.upper()
        super(Unidade, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('unidade_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('unidade_delete', args=[str(self.id)])
