# Revisão semanal

## Projeto Python-Django

Presença do modelo MVT
    - M - model: orientação a objetos que será convertida em BD
        - é um arquivo com nome models.py
    - V - view:  regras do negócios e todos os CRUD
        - é um arquivo com nome views.py
    - T - template: páginas html e css (com apoio do Bootstrap)

Projeto do sistema desenvolvido
    - todo projeto tem em comum:
        - core: pasta com os html da home ou do ambiente já logado do sistema
        - projeto: configuração do sistema
        - demais apps (subsistemas criados pela equipe ou pelo programador)


## Fluxo de desenvolvimento da app (subsistema)

    1) criar ou copiar app
    2) criar ou reutilizar/adaptar o models.py
    3) criar ou reutilizar/adaptar o views.py
    4) criar ou reutilizar/adaptar a pasta template
    5) criar ou reutilizar/adaptar o arquivo urls.py dentro do app
    6) atualizar o arquivo urls.py do projeto, avisando sobre o app
    7) liberar o acesso ao app em um menu ou página do sistema
        - core do sistema, pasta template
    8) adicionar em projeto/projeto/settings.py o app no campo INSTALLED_APPS
    9) gerar as migrações
        - python projeto/manage.py makemigrations -> gera os scritps do sql escolhido
        - python projeto/manage.py migrate        -> roda os scripts gerados e cria a tabela