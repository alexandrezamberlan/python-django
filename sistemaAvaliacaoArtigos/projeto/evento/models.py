from __future__ import unicode_literals

import os

from django.db import models
from django.dispatch import receiver
from django.urls import reverse


from utils.gerador_hash import gerar_hash

class EventoAtivoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Evento(models.Model):       
    nome = models.CharField('Nome do evento *', unique=True, db_index=True, max_length=150, help_text='* Campo obrigatório')
    tipo = models.ForeignKey('tipo_evento.TipoEvento', verbose_name= 'Tipo do evento *', on_delete=models.PROTECT, related_name='tipo_evento')
    instituicao = models.ForeignKey('instituicao.Instituicao', verbose_name= 'Instituição responsável pelo evento *', on_delete=models.PROTECT, related_name='instituicao')
    data_inicio = models.DateField('Data de início do evento *', max_length=10, help_text='Use dd/mm/aaaa')
    data_limite_trabalhos = models.DateField('Data limite para envio de trabalhos *', max_length=10, help_text='Use dd/mm/aaaa')
    coordenador = models.ForeignKey('usuario.Usuario', verbose_name= 'Coordenador responsável *', on_delete=models.PROTECT, related_name='coordenador')
    coordenador_suplente = models.ForeignKey('usuario.Usuario', verbose_name= 'Coordenador suplente', on_delete=models.PROTECT, related_name='coordenador_suplente', null=True, blank=True)
    email = models.EmailField('Email oficial da comissão científica *', max_length=100,help_text='Campo obrigatório. Email para contato dos membros que estão submetendo trabalhos.', null=True, blank=False)
    modelo_artigo = models.CharField('Qual o modelo para artigos? ', max_length=150, help_text='Informe o modelo, como ABNT, SBC, IEEE')
    arquivo_modelo = models.FileField('Carregue arquivo zipado com modelos', null=True, blank=True, upload_to='midias', help_text='Utilize arquivo compactado do tipo zip')
    is_active = models.BooleanField('Ativo', default=True, help_text='Se ativo, o evento está liberado para chamada de artigos')
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)

    objects = models.Manager()
    eventos_ativos = EventoAtivoManager()

    class Meta:
        ordering            =   ['-is_active','-data_limite_trabalhos','nome']
        verbose_name        =   'evento'
        verbose_name_plural =   'eventos'

    def __str__(self):
        return '%s | %s | %s' % (self.nome, self.data_limite_trabalhos.strftime("%d/%m/%Y"), self.instituicao.nome)

    def save(self, *args, **kwargs):        
        if not self.slug:
            self.slug = gerar_hash()
        self.nome = self.nome.upper()
        self.modelo_artigo = self.modelo_artigo.upper()        
        super(Evento, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('evento_update', kwargs={'slug': self.slug})

    @property
    def get_delete_url(self):
        return reverse('evento_delete', kwargs={'slug': self.slug})


#triggers para limpeza dos arquivos apagados ou alterados. No Django é chamado de signals
#deleta o arquivo fisico ao excluir o item midia
@receiver(models.signals.post_delete, sender=Evento)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.arquivo_modelo:
        if os.path.isfile(instance.arquivo_modelo.path):
            os.remove(instance.arquivo_modelo.path)

#deleta o arquivo fisico ao alterar o arquivo do item midia
@receiver(models.signals.pre_save, sender=Evento)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        obj = Evento.objects.get(pk=instance.pk)

        if not obj.arquivo_modelo:
            return False

        old_file = obj.arquivo_modelo
    except Evento.DoesNotExist:
        return False

    new_file = instance.arquivo_modelo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
