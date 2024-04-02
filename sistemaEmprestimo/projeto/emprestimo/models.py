from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.gerador_hash import gerar_hash
    
class Emprestimo(models.Model): 
    locador = models.ForeignKey('usuario.Usuario', verbose_name= 'Locador', on_delete=models.PROTECT)
    objeto = models.ManyToManyField('objeto.Objeto', verbose_name= 'Objeto(s) emprestado(s)')
    data_emprestimo = models.DateTimeField(_('Data do empréstimo '), max_length=10, help_text='Use dd/mm/aaaa')
    em_emprestimo = models.BooleanField(_('Selecione se o objeto estiver emprestado '), default=False)

    slug = models.SlugField('Hash',max_length= 200, null=True, blank=True)
    
    objects = models.Manager()
    
    class Meta:
        ordering            =   ['-em_emprestimo', 'locador']
        verbose_name        =   ('emprestimo')
        verbose_name_plural =   ('emprestimos')
        unique_together     =   [['locador','data_emprestimo']]

    def __str__(self):
        return "Objeto: %s. Pessoa: %s." % (self.objeto, self.locador)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        super(Emprestimo, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('emprestimo_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('emprestimo_delete', args=[str(self.id)]) 