# Sistema Avaliação de Artigos

<img width="1063" alt="telaPrincipal" src="https://github.com/alexandrezamberlan/python-django/assets/5599081/063d72b1-1a4c-4a14-a3fe-187d866bdefb">


- PENDÊNCIAS 
    - termo de uso e política de funcionamento
    - criar esquema de mandar email:
        - no autocadastro
        - quando submissão é realizada
        - quando resultado da avaliação é finalizada
        - pensar no app critério ou usar um conjunto de critérios padrão baseado na revista disciplinarum (UFN)???
        - ...
    - fazer logout quando o usuário conectado por 30 min ou quando fechar navegador
    - validar em evento se coordenador responsa'vel e coordenador suplemente são a mesma pessoa
    - na visão de coordenador, possibilitar que o usuário envie trabalhos mas para outros eventos, exceto para os eventos que coordenada. O mesmo para o coordenador responsável
    - disponibilizar app no servidor lapinf.ufn
        - mysql
        - gunicorn
        - nginx
        - certbot

- apps
    - usuario
        - tipos: administrador, coordenador de evento, ordinario (submete ou avalia)
        - nome
        - titulação (técnico, graduando, graduado, especialista, mestre, doutor)
        - email (chave primária)
        - celular
        - cpf
        - área (Ciências Humana, Ciências da Saúde, Ciências Sociais, Ciências Tecnológicas)
        - instituição (não tem vinculo com app instituição) - pedir pra não usar sigla
        - is_active
        - slug

        Obs.:
            - usuário faz autocadastro (exceto administrador)
                - colocar campo de aceite dos termos de uso
    
    - instituição
        - nome
        - sigla (opcional)
        - cidade
        - estado
        - país
        - is_active
        - slug

    - evento 
        - nome
        - tipo (congresso, simpósio, revista, capítulo de livro, ....)
        - instituição (relação com app instituição)
        - data do evento
        - coordenador do evento (relação com app usuario) - DEVE SER TIPO COORDENADOR EM USUÁRIO
        - coordenador suplente (opcional - relação com app usuario) - DEVE SER TIPO COORDENADOR EM USUARIO
        - email comissão científica
        - data limite de envio de trabalhos
        - arquivo com template para o evento
        - regras de publicação (criar app de documentos)
            - modelo do documento (arquivo template)
            - quantidade de páginas miníma e máxima
            - conteúdo do texto esperado (introdução, revisão bibliográfica, metodologia, resultados, conclusões)
        - is_active
        - slug
        - template de critérios (????)
    

    - submissão
        - responsável (usuário ordinário)
        - coautores (lista de usuários ordinários)
        - numero_maximo de autores
        - evento (relação com app evento)
        - data e hora da submissão (capturado automático)
        - enviar email de registro de submissão para o responsável
        - titulo (pensar no limite de palavras)
        - resumo (pensar no limite de caracteres, linhas ou palavras)
        - abstract (pensar no limite de caracteres, linhas ou palavras)
        - palavras-chave (pensar no limite de palavras)
        - categoria ou subárea do trabalho (???)
        - arquivo da versão de avaliação (sem autores ou identificação - .pdf)
        - arquivo da versão corrigida e aprovada (com autores ou identificação - .pdf)
        - arquivo do comitê de ética zipado (quando artigo trabalhar com seres humanos)
        - status (aprovado, reprovado, em correção, retirada pelo responsável)

    - avaliacao
        - submissao (relação com app submissao)
        
        - avaliador 1 (usuario ordinário)
        - avaliação dos critérios do avaliador 1 
        - parecer do avaliador 1
        - recomendação da publicação (1 a 5, sendo 5 publicação certa, 1 não publicar)
        - data da finalização da avaliação
        - arquivo do texto corrigido

        - avaliador 2 (usuario ordinário)
        - avaliação dos critérios do avaliador 2
        - parecer do avaliador 2
        - recomendação da publicação (1 a 5, sendo 5 publicação certa, 1 não publicar)
        - data da finalização da avaliação
        - arquivo do texto corrigido
        
        - avaliador 3 (opcional | usuario ordinário)
        - avaliação dos critérios do avaliador 3
        - parecer do avaliador 3
        - recomendação da publicação (1 a 5, sendo 5 publicação certa, 1 não publicar)
        - data da finalização da avaliação
        - arquivo do texto corrigido

        media da recomendação dos avaliadores

Sugestões de CSS
    - https://bootsnipp.com/snippets/eNe4v
    - https://adminlte.io/themes/AdminLTE/index2.html
    - https://bootswatch.com/3/

Icons bootstrap - https://www.w3schools.com/icons/bootstrap_icons_glyphicons.asp
