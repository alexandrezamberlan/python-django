# Sistema Python Django para Triagem Covid19
Sistema Web para triagem de atendimento de pacientes com possível Covid19

## Preparando o ambiente para desenvolvimento
> ***Ocorrência:*** A cada nova instalação do Sistema Operacional.

### Instalação do PIP (Python Index Package):
```shell
#Linux/Mac OSx:
sudo easy_install pip

#Distribuições Linux derivados do Debian - Ex.: Ubuntu:
sudo apt-get install python-pip
```

### Instalação do Virtualenv (Ferramenta gestora de ambientes Python virtualizados isolados):
```shell
#Linux/Mac OSx:
pip install virtualenv

#Distribuições Linux derivados do Debian - Ex.: Ubuntu:
sudo apt-get install python-virtualenv
```
### Instalação do GIT (Habilitar o Sistema Operacional para trabalhar com controle de versão GIT)
```shell
#Mac OS/x:
http://sourceforge.net/projects/git-osx-installer/

#Distribuições Linux derivados do Debian - Ex.: Ubuntu:
sudo apt-get install git
```

## Criação do projeto:
> Passo a passo com principais atividades necessárias para iniciar um projeto. Consulte a documentação oficial do Django para mais detalhes https://www.djangoproject.com/start/

> ***Objetivo:*** Projeto Django rodando localmente, versionado com Git e distribuído na plataforma Github

```shell
### Sugere-se, primeiro criar a ideia do projeto do Git (GitHub, Bitbucket ou GitLab). Criar os arquivos .gitignore e README.md

### Clonar o projeto via Git no seu diretório (pasta) escolhido
git clone http://............ 

### Acessar a pasta do projeto clonado
cd pastaClonada

### Criando uma virtualenv com Python (ambiente isolado) - Ambiente localizado no diretório venv
virtualenv -p python3 venv

### Ativando a virtualenv
source venv/bin/activate

### Caso esteja no Windows (principalmente o 10), para criar e ativar a venv, use estes passos
python3 -m venv venv 
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
venv\Scripts\activate 

### Instalando os softwares dentro do arquivo requirements.txt
pip install -r requirements.txt

### Iniciando um projeto Django
django-admin.py startproject projeto

### Acessando o diretório projeto
cd projeto

### Configurando a linguagem e data/hora do projeto. Edite o arquivo: projeto/settings.py
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo' 

SUGESTÃO: copie o projeto/settings.py para dentro de seu projeto

### Rodar a migração para criação das tabelas básicas do Django no Banco de dados
python manage.py migrate

### Criação de uma aplicação chamada core que controla o fluxo do nosso sistema
python manage.py startapp core

### Criacao da view responsável pela exibição da home/index na app core
#edite o arquivo core/views.py e certifique-se que contenha:

from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.base import TemplateView

from utils.decorators import LoginRequiredMixin

class HomeView(LoginRequiredMixin, TemplateView):
	template_name = 'core/home.html'

class AboutView(TemplateView):
	template_name = 'core/about.html'


### crie o home.html em core/templates/core/home.html (será preciso criar os diretórios)

{% extends 'core/base.html' %}
{% load bootstrap3 %}
{% load static %}

{% block title %}
      <a href="https://www.ufn.edu.br" target="_blank"><img src="{% static 'core/img/logoUFN_hor.jpg' %}"
      class="img-responsive" style="max-width: 120px;"></a>
{% endblock %}

{% block content %}

{% if user.is_authenticated %}
      <center>
            <h2>Sistema de Triagem Covid 19</h2>
            <h3>Laboratório de Práticas</h3>
	</center>
{% endif %}

{% endblock %}


### crie o arquivo urls.py em: core/urls.py - Ele é responsável pela identificação da view responsável para cada URL pertencente a app core

### edite o arquivo core/urls.py com o seguinte conteúdo:

from __future__ import unicode_literals
from django.conf.urls import url
from .views import HomeView, AboutView, HomeRedirectView

urlpatterns = [
   url(r'^$', HomeRedirectView.as_view(), name='home_redirect'),
   url(r'^home$', HomeView.as_view(), name='home'),
   url(r'^about$', AboutView.as_view(), name='about'),
]

### instale a app core no projeto editando o arquivo projeto/settings.py adicionando na lista INSTALLED_APPS como no exemplo:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'core',
]

### habilite o gerenciador de URLs do projeto para trabalhar com as URLs da app core, para isto, edite o arquivo projeto/urls.py importando o urls do core:

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('core.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

### url para arquivos de media quando em desenvolvimento
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, 
    document_root = settings.STATIC_ROOT)    


### sempre que criar um app, rodar makemigrations (gera os scripts para o banco de dados) e migrate (roda o script)
python manage.py makemigrations core

python manage.py migrate core

### neste ponto a sua home já pode ser exibida no navegador

### rodando o servidor web de desenvolvimento (dentro do diretório projeto)
python manage.py runserver

### acessando via navegador
http://localhost:8000
```

## Criando modelo para persistir no Banco de Dados, Instalando a app no Django Admin (Painel), Buscando os registros do modelo numa view e mostrando no HTML
```shell
### no diretório projeto, crie as apps: usuario, instituicao, ....

python manage.py startapp usuario
python manage.py startapp instituicao
python manage.py startapp ....

### edite o arquivo models.py dentro da app criada, adicionando a classe referente a app. Repita isso para cada models de aplicação criada

### edite o arquivo views.py dentro da app criada, adicionando os métodos referentes a app. Repita isso para cada classe de aplicação criada. Por exemplo:

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ClasseCriada

class ClasseCriadaListView(LoginRequiredMixin, ListView):
	model = ClasseCriada

class ClasseCriadaCreateView(LoginRequiredMixin, CreateView):
	model = ClasseCriada
	fields = ['campo1', 'campo2', 'campo3' ,'....']
	success_url = 'app_criada_list'

class ClasseCriadaUpdateView(LoginRequiredMixin, UpdateView):
	model = ClasseCriada
	fields = ['campo1', 'campo2', 'campo3' ,'....']
	success_url = 'app_criada_list'

class InjuriaDeleteView(LoginRequiredMixin, DeleteView):
	model = ClasseCriada
	fields = ['campo1', 'campo2', 'campo3' ,'....']


### instale a app criada no projeto editando o arquivo projeto/settings.py adicionando na lista INSTALLED_APPS:

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'core',
	'usuario',
	'instituicao',
	'...'
]

### habilite o gerenciador de URLs do projeto para trabalhar com as URLs da app criada. Para isto, edite o arquivo projeto/urls.py importando o urls da app criada:

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('core.urls')),
    url(r'usuario/', include('usuario.urls')),
    url(r'instituicao/', include('instituicao.urls')),
    url(r'.../', include('....urls')),
    url(r'^accounts/', include('django.contrib.auth.urls'))
]

### crie o arquivo urls.py dentro da pasta da app criada. Por exemplo:

from django.conf.urls import url
from .views import ClasseCriadaListView, ClasseCriadaCreateView
from .views import ClasseCriadaUpdateView, ClasseCriadaDeleteView

urlpatterns = [
	url(r'list/$', ClasseCriadaListView.as_view(), name='app_criada_list'),
	url(r'cad/$', ClasseCriadaCreateView.as_view(), name='app_criada_create'),
	url(r'(?P<pk>\d+)/$', ClasseCriadaUpdateView.as_view(), name='app_criada_update'),
	url(r'(?P<pk>\d+)/delete/$', ClasseCriadaDeleteView.as_view(), name='app_criada_delete'),
]

### criar script para migração do Banco de Dados dos modelos das apps (script que cria as tabelas necessárias para atender o modelo especificado)

python manage.py makemigrations core
python manage.py makemigrations usuario
python manage.py makemigrations ...

### comando no terminal para rodar as migrações da app core no Banco de Dados
python manage.py migrate core
python manage.py migrate usuario
python manage.py migrate ....

### Criando o banco de dados e o 1o usuario do banco: com a venv levantada, na pasta projeto, rodar:
python manage.py shell

### PARA VISUALIZAR, SE NECESSÁRIO, OS USUÁRIOS DO MYSQL
SELECT user FROM mysql.user;

### criando o banco
CREATE DATABASE nomeDoSistema_db;

CREATE USER ‘nomeDoSistema’@‘localhost' IDENTIFIED BY ‘senhaDesejada’;

GRANT ALL PRIVILEGES ON nomeDoSistema_db.* TO ‘nomeDoSistema’@‘localhost' IDENTIFIED BY 'senhaDesejada';

### criando o primeiro usuário
from usuario.models import Usuario
u = Usuario()
u.nome = 'Nome do Usuário'
u.tipo = 'ADMINISTRADOR'
u.email = 'projetos@ufn.edu.br'
u.is_active = True
u.cpf = '99999999999'
u.save()
u.set_password('projetos@ufn.edu.br')
u.save()

```

