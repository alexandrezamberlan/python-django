Cloud Computing - Compartilhamento de recursos
    - Memória Secundária
    - Processador e Memória Principal
    - Processos executando fora do local
    - Sistema Web
        - Cliente-Servidor
            - Monolítica: 
                - Desenvolvimento Python-Django-Bootstrap
                    - Python: linguagem OO
                    - Django: framework com MOR (Mapeamento Objeto Relacional)
                                - com recursos úteis para reuso
                    - Bootstrap: framework html e css

            - Serviços:
                Exemplo: Servidor LapInf (máquina virtual)
                    - 4 Gb RAM
                    - 1 Tb Memória Secundária
                    - 1.33 Ghz de cpu
                    - Ubuntu 20.0 server
                        - firewall - ufw
                            - ssh
                            - http
                            - smtp
                            - pop/imap
                        - banco de dados - mysql -> postgree
                        - servidores páginas http e http+py -> gunicorn + nginx
                        - pastas de sistemas web com devidas permissões
                            - /var/www/site/pastaSistema
                            Exemplo:
                                /var/www/tfgonline.lapinf.ufn.edu.br/tfgonline
                    - Sistemas Web desenvolvidos
                        /var/www/site/pastaSistema
                            - a pastaSistema é um repositório Git
                                .gitignore  -> relação de arquivos e pastas que não irão transitar ao servidor git
                                .env        -> arquivo python-django com variáveis de ambiente e senhas
                                venv        -> ambiente virtual criado para este sistema
                                                    -> pacotes, bibliotecas, serviços específicos ao sistema Web em questão
                                requeriments.txt -> arquivo com a relação de pacotes e bibliotecas a serem instaladas na venv
                                projeto     -> pasta contendo o projeto ou o sistema django
                                    Organização da pasta do sistema baseada no Modelo MVT
                                        - Model     -> orientação a objetos ou banco de dados
                                        - View      -> regras ou funcionalidades de negócio
                                        - Template  -> html e css

                                    pastas internas ao projeto:
                                        - projeto: arquivos de configuração do sistema
                                        - core: arquivos de controle e de exibição inicial do sistema
                                        - pastaAPP : subsistema com um CRUD completo
                                            arquivo models.py
                                            arquivo views.py
                                            pasta Template e dentro outra pasta com o nome pastaAPP

                    - Política de backup
                        - crontab   -> backup agendado em arquivo em outro usuário e em pasta específica

                    
        