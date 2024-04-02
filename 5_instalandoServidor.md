Passos para disponibilizar sistema em servidor linux

Acesso remoto via SSH

Necessário a instalação e configuração do:
    - Gunicorn - https://gunicorn.org/ - is a Python WSGI HTTP Server for UNIX.
    - Nginx - https://www.nginx.com/ - is a free, open-source, high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server.

Clonar o projeto na pasta desejada, em geral, uma boa prática é em /var/www/urlCriada/nomeProjetoClonado

Criar e levantar a venv, e instalar os requirements.txt

============
GUNICORN 

criar o arquivo /etc/systemd/system/nomeProjeto.service

[Unit]
Description=nomeProjeto daemon
After=network.target

[Service]
User=usuarioServidor
Group=www-data
WorkingDirectory=pastaServidor/nomeProjeto/projeto
ExecStart=pastaServidor/nomeProjeto/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:pastaServidor/nomeProjeto/projeto/nomeProjeto.sock projeto.wsgi:application

============

Iniciar o parser gunicorn:
sudo systemctl start nomeProjeto

Adicionar o sistema como serviço reconhecido no sistema:
sudo systemctl enable nomeProjeto

============
Nginx

Esse é o roteiro para criar outros serviços virtuais, ai e só substituir exemplo.com pelo  domínio que tu vai utilizar sem www (por exemplo, comic.labinf.ufn.edu.br)
 
Crie o diretório para examplo.com como a seguir, usando o flag -p para criar qualquer diretório pai necessário:
 
sudo mkdir -p pastaServidor/examplo.com/
  
Para que o Nginx sirva esse conteúdo, é necessário criar um bloco de servidor com as diretivas corretas. 
Em vez de modificar o arquivo de configuração padrão diretamente, vamos criar um novo em /etc/nginx/sites-available/examplo.com:
 
sudo vim /etc/nginx/sites-available/exemplo.com
Cole dentro o seguinte bloco de configuração, que é similar ao padrão, mas atualizado para nosso novo diretório e nome de domínio:
 
/etc/nginx/sites-available/exemplo.com
 
server {
        server_name comic.lapinf.ufn.edu.br www.comic.lapinf.ufn.edu.br;
        client_body_in_file_only clean;
        client_body_buffer_size 32K;
        client_max_body_size 2512M;


        #aceitar arquivos grande via get
        client_header_buffer_size 3232k;
        large_client_header_buffers 4 3232k;
        sendfile on;
        send_timeout 900s;
        location = /favicon.ico { access_log off; log_not_found off; }

        location /static {
                expires 30d;
                access_log off;
                break;
                alias /var/www/comic.lapinf.ufn.edu.br/comic/projeto/projeto/static;
        }

        location / {
                client_max_body_size 2048M;
                include proxy_params;
                proxy_pass http://unix:/var/www/comic.lapinf.ufn.edu.br/comic/comic.sock;
        }
} 
Observe que atualizamos a configuração root para corresponder ao nosso novo diretório e 
server_name ao nosso nome de domínio.
 
A seguir, vamos ativar o arquivo através da criação de um link dele para o diretório sites-enabled, 
a partir do qual o Nginx lê durante a inicialização:
 
sudo ln -s /etc/nginx/sites-available/exemplo.com /etc/nginx/sites-enabled/
 
Depois, teste para certificar-se de que não existem erros de sintaxe em quaisquer de seus arquivos do Nginx:
 
sudo nginx -t
Salve e feche o arquivo quando tiver terminado.
 
Se não houver problemas, reinicie o Nginx para ativar suas alterações:
 
sudo systemctl restart nginx

=============================
 
Obtendo um Certificado SSL
 
sudo certbot --nginx -d exemplo.com -d www.exemplo.com
 
Se isso for bem sucedido, o certbot perguntará como você gostaria de definir suas configurações de HTTPS.
Usa 2 para sempre redirecionar para SSL
Output
Please choose whether or not to redirect HTTP traffic to HTTPS, removing HTTP access.
-------------------------------------------------------------------------------
1: No redirect - Make no further changes to the webserver configuration.
2: Redirect - Make all requests redirect to secure HTTPS access. Choose this for
new sites, or if you're confident your site works on HTTPS. You can undo this
change by editing your web server's configuration.
-------------------------------------------------------------------------------
Select the appropriate number [1-2] then [enter] (press 'c' to cancel):
Selecione a sua escolha e pressione ENTER. A configuração será atualizada, e o Nginx irá recarregar para pegar as novas configurações. O certbot irá terminar com uma mensagem informando que o processo foi bem-sucedido e onde os seus certificados estão armazenados:
 
Output
IMPORTANT NOTES:
- Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/exemplo.com/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/exemplo.com/privkey.pem
   Your cert will expire on 2018-07-23. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot again
   with the "certonly" option. To non-interactively renew *all* of
   your certificates, run "certbot renew"
- Your account credentials have been saved in your Certbot
   configuration directory at /etc/letsencrypt. You should make a
   secure backup of this folder now. This configuration directory will
   also contain certificates and private keys obtained by Certbot so
   making regular backups of this folder is ideal.
- If you like Certbot, please consider supporting our work by:
 
   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
  Donating to EFF:                    https://eff.org/donate-le
 

============

PARA VISUALIZAR, SE NECESSÁRIO, OS USUÁRIOS DO MYSQL
SELECT user FROM mysql.user;

CREATE DATABASE nomeDoSistema_db;

CREATE USER ‘nomeDoSistema’@‘localhost' IDENTIFIED BY ‘senhaDesejada’;

GRANT ALL PRIVILEGES ON nomeDoSistema_db.* TO ‘nomeDoSistema’@‘localhost' IDENTIFIED BY 'senhaDesejada';

============
Criando o primeiro usuário

na pasta projeto do sistema, com a venv ativa,
rodar migrate


from usuario.models import Usuario
u = Usuario()
u.nome = 'SADEPI'
u.tipo = 'ADMINISTRADOR'
u.email = 'projetos@ufn.edu.br'
u.is_active = True
u.cpf = '99999999999'
u.save()
u.set_password('projetos@ufn.edu.br')
u.save()

=======
.env
DATABASE_URL=mysql://sadepi:sadepi2018$@127.0.0.1:3306/sadepi_db


