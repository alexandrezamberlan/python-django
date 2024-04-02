from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.gerador_hash import gerar_hash

class FornecedorAtivoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Fornecedor(models.Model):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    FORNECEDOR_TIPO = (
        ('BRASILEIRO', 'Brasileiro'),
        ('EXTERNO', 'Externo'),
    )
    
    nome = models.CharField('Nome do fornecedor *',  max_length=100, help_text='* Campo obrigatório')
    cnpj = models.CharField('CNPJ *', unique=True, max_length=15, help_text='* Campo obrigatório')
    cidade = models.CharField('Cidade *', max_length=100, help_text='* Campo obrigatório')   
    tipo_fornecedor = models.CharField('Tipo de fornecedor *', max_length=10, choices=FORNECEDOR_TIPO, help_text='* Campo obrigatório')
    is_active = models.BooleanField('Ativo', default=True, help_text='Se ativo, o fornecedor pode ser usado no sistema')
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)

    objects = models.Manager()
    fornecedores_ativos = FornecedorAtivoManager()

    
    class Meta:
        ordering            =   ['-is_active','tipo_fornecedor', 'nome']
        verbose_name        =   'fornecedor'
        verbose_name_plural =   'fornecedores'

    def __str__(self):
        return '%s - %s. %s' % (self.cnpj, self.nome, self.tipo_fornecedor)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        self.nome = self.nome.upper()
        self.cidade = self.cidade.upper()        
        super(Fornecedor, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('fornecedor_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('fornecedor_delete', args=[str(self.id)])
