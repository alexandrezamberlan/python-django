from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.gerador_hash import gerar_hash

class InstituicaoAtivoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Instituicao(models.Model):
    nome   = models.CharField('Nome descritivo da instituição *', unique=True, max_length=100, help_text='* Campo obrigatório')
    sigla  = models.CharField('Sigla da instituição ', max_length=100, help_text='Opcional')
    cidade = models.CharField('Cidade no qual reside *', max_length=50, help_text='* Campo obrigatório')
    estado = models.CharField('Estado no qual reside *', max_length=50, help_text='* Campo obrigatório')
    pais   = models.CharField('País no qual reside *', max_length=20, help_text='* Campo obrigatório.')
    
    is_active = models.BooleanField(('Ativo'), default=True, help_text='Se ativo, a instituição pode ser referenciada no sistema')
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)

    objects = models.Manager()
    instituicoes_ativas = InstituicaoAtivoManager()

    class Meta:
        ordering            =   ['-is_active','nome']
        verbose_name        =   'instituição'
        verbose_name_plural =   'instituições'

    def __str__(self):
        return '%s - %s' % (self.nome, self.sigla)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        self.nome = self.nome.upper()
        self.sigla = self.sigla.upper()
        super(Instituicao, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('instituicao_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('instituicao_delete', args=[str(self.id)])
