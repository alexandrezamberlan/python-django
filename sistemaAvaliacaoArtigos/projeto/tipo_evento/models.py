from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


from utils.gerador_hash import gerar_hash

class TipoEventoAtivoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class TipoEvento(models.Model):       
    descricao = models.CharField('Tipo de evento *', unique=True, db_index=True, max_length=100, help_text='* Campo obrigatório')
    
    is_active = models.BooleanField('Ativo', default=True, help_text='Se ativo, o tipo pode ser usada no sistema')
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)

    objects = models.Manager()
    tipos_eventos_ativos = TipoEventoAtivoManager()

    class Meta:
        ordering            =   ['-is_active','descricao']
        verbose_name        =   'Descrição'
        verbose_name_plural =   'Descrições'

    def __str__(self):
        return self.descricao

    def save(self, *args, **kwargs):        
        if not self.slug:
            self.slug = gerar_hash()
        
        self.descricao = self.descricao.upper()           
        super(TipoEvento, self).save(*args, **kwargs)
        

    @property
    def get_absolute_url(self):
        return reverse('tipo_evento_update', kwargs={'slug': self.slug})

    @property
    def get_delete_url(self):
        return reverse('tipo_evento_delete', kwargs={'slug': self.slug})
