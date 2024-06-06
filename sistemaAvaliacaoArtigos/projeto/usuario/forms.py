from django import forms
from django.db import models

from .models import Usuario

class BuscaUsuarioForm(forms.Form):    
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TIPOS_USUARIOS = (
        (None, '-----'),
        ('ADMINISTRADOR', 'Administrador'),
        ('COORDENADOR', 'Coordenador de Evento' ),
        ('MEMBRO', 'Membro'),
    )
   #(técnico, graduando, graduado, especialista, mestre, doutor)
    TITULACAO = (
        (None, '-----'),
        ('TECNICO', 'Técnico'),
        ('GRADUANDO', 'Graduando' ),
        ('GRADUADO', 'Graduado' ),        
        ('ESPECIALISTA', 'Especialista'),
        ('MESTRE', 'Mestre' ),
        ('DOUTOR', 'Doutor' ),        
    )

    #(Ciências Humana, Ciências da Saúde, Ciências Sociais, Ciências Tecnológicas)
    AREA = (
        (None, '-----'),
        ('HUMANAS', 'Ciências Humanas'),
        ('SAUDE', 'Ciências da Saúde' ),
        ('SOCIAIS', 'Ciências Sociais' ),        
        ('TECNOLOGICA', 'Ciências Tecnológicas'),        
    )

    tipo = forms.ChoiceField(label='Tipo de usuário', choices=TIPOS_USUARIOS, required=False)
    titulacao = forms.ChoiceField(label='Titulação', choices=TITULACAO, required=False)
    area = forms.ChoiceField(label='Área de interesse', choices=AREA, required=False)
    
    
class UsuarioRegisterForm(forms.ModelForm):
    TIPOS_USUARIOS = (
        ('MEMBRO', 'Membro'),
    )
    #(técnico, graduando, graduado, especialista, mestre, doutor)
    TITULACAO = (
        ('TECNICO', 'Técnico'),
        ('GRADUANDO', 'Graduando' ),
        ('GRADUADO', 'Graduado' ),        
        ('ESPECIALISTA', 'Especialista'),
        ('MESTRE', 'Mestre' ),
        ('DOUTOR', 'Doutor' ),        
    )

    #(Ciências Humana, Ciências da Saúde, Ciências Sociais, Ciências Tecnológicas)
    AREA = (
        ('HUMANAS', 'Ciências Humanas'),
        ('SAUDE', 'Ciências da Saúde' ),
        ('SOCIAIS', 'Ciências Sociais' ),        
        ('TECNOLOGICA', 'Ciências Tecnológicas'),        
    )

    tipo = forms.ChoiceField(label='Tipo *',choices=TIPOS_USUARIOS, help_text='Este processo cadastra somente membros', required=True)
    nome = forms.CharField(label='Nome completo *', help_text='* Campos obrigatórios',required=True)
    titulacao = forms.ChoiceField(label='Titulação *',choices=TITULACAO, help_text='Selecione a maior titulação', required=False)
    area = forms.ChoiceField(label='Área de pesquisa do usuário *', choices=AREA, help_text='Escolha área de interesse de trabalho',required=True)
    instituicao = forms.CharField(label='Instituição a que pertence *', help_text='Registre a instituição, ou universidade, ou empresa',required=True)
    email = forms.EmailField(label='Email *', help_text='Use o email válido. Será usado para acessar sistema e recuperar senha!',required=True)
    celular = forms.CharField(label='Número celular com DDD *', max_length=11, help_text="Use DDD, por exemplo 55987619832",required=True)
    cpf = forms.CharField(label='CPF *',required=True)    
    password = forms.CharField(label= "Senha *", widget=forms.PasswordInput,required=True)
        
    class Meta:
        model = Usuario
        fields = ['tipo','nome','titulacao', 'area', 'instituicao', 'email', 'celular', 'cpf', 'password']
