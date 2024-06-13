from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.urls import reverse


from utils.gerador_hash import gerar_hash


class AvisoAtivoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Aviso(models.Model):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    DESTINO = (
        ('TODOS', 'Todos'),
        ('COORDENADOR', 'Coordenador de Evento' ),
        ('MEMBRO', 'Membro' ),        
    )    

    titulo = models.CharField('Título do aviso *', unique=True, max_length=100, db_index=True, help_text='* Campos obrigatórios')
    texto = models.TextField('Texto da notícia *', max_length=500, help_text='Máximo de 500 caracteres')
    data = models.DateField('Data do aviso', auto_now=True)
    destinatario = models.CharField('Destinatários *', max_length=20, choices=DESTINO, default="TODOS")
    enviado = models.BooleanField('Selecione para enviar aviso por email aos destinatários', default=False, help_text='Se marcado, aviso é enviado uma vez aos detinatários ativos')
    is_active = models.BooleanField('Selecione para publicar na home dos usuários o aviso', default=True, help_text='Se ativo, o aviso aparece na home de atletas')
    
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)

    objects = models.Manager()
    ativos = AvisoAtivoManager()
    
    class Meta:
        ordering            =   ['-data','titulo']
        verbose_name        =   'aviso'
        verbose_name_plural =   'avisos'

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        self.titulo = self.titulo.upper()
        super(Aviso, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('aviso_update', kwargs={'slug': self.slug})

    @property
    def get_delete_url(self):
        return reverse('aviso_delete', kwargs={'slug': self.slug})

    @property
    def get_envia_email_url(self):
        return reverse('aviso_envia_email', kwargs={'slug': self.slug})
