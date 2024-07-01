from django import forms
from django.db import models

from evento.models import Evento
from usuario.models import Usuario
from .models import Submissao


class SubmissaoForm(forms.ModelForm):
    responsavel = forms.ModelChoiceField(label='Autor responsável *', queryset=Usuario.usuarios_ativos.all())
    evento = forms.ModelChoiceField(label='Evento para a submissão *', queryset=Evento.eventos_ativos.all())

    class Meta:
        model = Submissao
        fields = ['responsavel', 'evento', 'titulo', 'resumo', 'abstract', 'palavras_chave', 'arquivo_sem_autores', 'arquivo_final', 'arquivo_comite_etica', 'status','observacoes', 'is_active']


class BuscaSubmissaoForm(forms.Form):     
    STATUS = (
        (None, '-----------'),
        ('EM EDICAO', 'Em edição'),
        ('EM ANALISE', 'Em análise'),
        ('EM CORRECAO', 'Em correção' ),        
        ('APROVADO', 'Aprovado' ),
        ('RETIRADO PELO RESPONSAVEL', 'Retirado pelo responsável'),
        ('RETIRADO PELO COORDENADOR', 'Retirado pelo coordenador' ),
        ('REPROVADO', 'Reprovado' ),  
    )         
    
    situacao = forms.ChoiceField(label='Status da submissão', choices=STATUS, required=False)
    pesquisa = forms.CharField(label='Pesquisa livre', required=False)
    
    
    