# Criando um projeto Python-Django
1) criar projeto ou repositório no GitHub
2) clonar projeto e criar .gitignore
3) criar a venv
    python -m venv venv
4) ativar a venv    (deactivate desativa a venv)
    windows ->  .\venv\Scripts\activate
    linux   ->  source venv/bin/activate

5) instalar pacotes via pip
    python -m pip install python-django (exemplo)

6) criar o arquivo requirements.txt ------------- pip freeze (lista os pacotes instalados)
    pip freeze > requirements.txt


# Clonando um projeto completo Python-Django

1) clonar projeto
2) criar e ativar a venv
3) instalar os pacotes em requirements.txt
    python -m pip install -r requirements.txt