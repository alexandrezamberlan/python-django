# Projeto Django

    ## Estrutura de diretório/pastas

    projeto
        - projeto
            - settings.py   -> configuração do sistema
            - urls.py       -> roteamento geral
        - core
            - models.py
            - urls.py
            - views.py
            - template
                - core
                    html e css
        - usuario
            - models.py
            - urls.py       -> roteamento local
            - views.py      -> regras de negócios - CRUD e validações
            - forms.py
            - template
                - usuario
                    - usuario_list.html
                    - usuario_form.html
                    - usuario_delete.html
        - utils             -> Classes e métodos de ajuda

    ## Shell do Django

    - Ambiente terminal util ou utilizavel depois que a venv estiver ativa com todos os pacotes instalados.
    - Rodar código python (listas) para trabalha o CRUD de um app

    - rodando o shell
        (venv) c:\projeto>python projeto\manage.py shell

    - Principal função: criar o primeiro usuário do sistema

    1) entrar no shell
    2) importar a classe Usuario
        from usuario.models import Usuario
    3) instanciar um objeto tipo Usuario
        u = Usuario()
    4) depositar os principais valores de atributos, exceto senha/password
    5) salvar o objeto Usuario criado
        u.save()
    6) definir senha para o usuário criado
        u.set_password('uma senha forte')
    7) salvar novamente o usuário com a senha criada

