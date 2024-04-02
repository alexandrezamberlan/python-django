from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.gerador_hash import gerar_hash

class MedicamentoAtivoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Medicamento(models.Model):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TIPOS_TARJAS = (
        ('BRANCA', 'Branca'),
        ('AMARELA', 'Amarela'),
        ('VERMELHA', 'Vermelha'),
        ('PRETA', 'Preta'),
    )
    TIPOS_MEDICAMENTOS = (
        ('CÁPSULA', 'Cápsula'),
        ('COMPRIMIDO', 'Comprimido'),
        ('LÍQUIDO', 'Líquido')        
    )

    nome_real = models.CharField('Nome real do medicamento *', unique=True, max_length=100, help_text='* Campo obrigatório')
    nome_fantasia = models.CharField('Nome fantasia do medicamento *', max_length=100, help_text='* Campo obrigatório')
    tarja = models.CharField('Tarja do medicamento *', max_length=10, choices=TIPOS_TARJAS, help_text='* Campo obrigatório')
    tipo = models.CharField('Tipo do medicamento *', max_length=10, choices=TIPOS_MEDICAMENTOS, help_text='* Campo obrigatório')
    quantidade = models.CharField('Quantidade do medicamento *', max_length=20, help_text='Informe a quantidade e a unidade. Por exemplo, 75 mg ou 10 ml ou 15 comprimidos.')
    fornecedor = models.ForeignKey('fornecedor.Fornecedor', verbose_name= 'Fabricante do medicamento', null = True, blank= False, on_delete=models.PROTECT, related_name='fornecedor')

    is_active = models.BooleanField(_('Ativo'), default=True, help_text='Se ativo, o curso pode ser usado no sistema')
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)

    objects = models.Manager()
    medicamentos_ativos = MedicamentoAtivoManager()

    
    class Meta:
        ordering            =   ['-is_active','tarja', 'nome_real']
        verbose_name        =   'medicamento'
        verbose_name_plural =   'medicamentos'

    def __str__(self):
        return '%s - %s' % (self.nome_real, self.nome_fantasia)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        self.nome_real = self.nome_real.upper()
        self.nome_fantasia = self.nome_fantasia.upper()
        super(Medicamento, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('medicamento_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('medicamento_delete', args=[str(self.id)])
