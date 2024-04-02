from __future__ import unicode_literals

import os

from django.conf import settings
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.gerador_hash import gerar_hash
    
class Objeto(models.Model):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TIPOS_OBJETOS = (
        ('LIVRO', 'Livro'),
        ('JOGO ELETRÔNICO', 'Jogo Eletrônico' ),
        ('VESTUÁRIO', 'Vestuário' ),
    )
    
    codigo = models.CharField(_('Código do objeto *'), unique=True, max_length=20, help_text='* Campos obrigatórios')
    tipo = models.CharField(_('Tipo do objeto *'), max_length=15, choices=TIPOS_OBJETOS, help_text='* Campos obrigatórios')
    descricao = models.CharField(_('Detalhes do objeto (resumo ou o título) *'), max_length=100, help_text='* Campos obrigatórios')
    valor = models.CharField(_('Valor do objeto'), max_length=20, null=True, blank=True)
    arquivo_foto = models.FileField(_('Foto do objeto'), null=True, blank=True, upload_to='midias', help_text='Tamanho máximo de 64MB')
    slug = models.SlugField('Hash',max_length= 200, null=True, blank=True)
    
    objects = models.Manager()
    
    class Meta:
        ordering            =   ['codigo','descricao']
        verbose_name        =   ('objeto')
        verbose_name_plural =   ('objetos')

    def __str__(self):
        return "Objeto: %s. Tipo: %s." % (self.descricao, self.tipo)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        self.codigo = self.codigo.upper()
        self.descricao = self.descricao.upper()
        super(Objeto, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('objeto_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('objeto_delete', args=[str(self.id)])
    
#triggers para limpeza dos arquivos apagados ou alterados. No Django é chamado de signals
#deleta o arquivo fisico ao excluir o item da pasta midias
@receiver(models.signals.post_delete, sender=Objeto)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.arquivo_foto:
        if os.path.isfile(instance.arquivo_foto.path):
            os.remove(instance.arquivo_foto.path)

#deleta o arquivo fisico ao alterar o arquivo da pasta midia
@receiver(models.signals.pre_save, sender=Objeto)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        obj = Objeto.objects.get(pk=instance.pk)

        if not obj.arquivo_foto:
            return False

        old_file = obj.arquivo_foto
    except Objeto.DoesNotExist:
        return False
