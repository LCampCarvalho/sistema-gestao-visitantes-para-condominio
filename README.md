# sistema-gestao-visitantes-para-condominio 🚀:smile:

Este sistema de gestão de condomínio foi desenvolvido em Python, utilizando Tkinter para a interface gráfica e SQLite como banco de dados. 
Ele permite gerenciar e monitorar visitantes e veículos, registrando suas entradas e saídas no condomínio e envia alertas em formato de e-mail.
Todos os registros são armazenados no banco de dados, com a opção de excluir esses dados posteriormente, conforme necessário.

##  Funcionalidades 

Funcionalidades principais:

✔ Registro de Visitantes: Cadastre visitantes com informações como nome, CPF, apartamento, data de visita e hora de entrada. Também é possível registrar a hora de saída.
✔ Registro de Veículos: Cadastre veículos informando placa, modelo, cor, apartamento e hora de entrada. A saída pode ser registrada posteriormente.
✔ Visualização de Visitantes e Veículos Presentes: Veja os visitantes e veículos que ainda estão no condomínio (ou seja, aqueles que ainda não tiveram sua saída registrada).
✔ Exclusão de Registros: Exclua registros de visitantes e veículos do sistema com base no CPF ou placa.

## Tecnologias utilizadas

✔ Python
✔ SQlite
✔ Tkinter
✔ Smtplib 

## Estrutura do Projeto

O sistema é composto por duas partes principais:

✔ Back-end (Banco de Dados): O banco de dados utiliza SQLite para armazenar os registros de visitantes e veículos.
✔ Front-end (Interface Gráfica): A interface gráfica foi construída com Tkinter, oferecendo uma interação simples e intuitiva para o usuário.

## Arquivo principal

✔ main.py: Contém a lógica do programa, incluindo a interface gráfica (com Tkinter) e as funções de manipulação de dados 
  (inserção, consulta, atualização e exclusão no banco de dados SQLite).

## Arquivo de banco de dados: gestao_condominio.db
  
✔ Banco de dados SQLite: Criado automaticamente na primeira execução do sistema. Ele armazena todas as informações dos visitantes e veículos.


## Como Executar o Projeto:

###Siga os passos abaixo para executar o sistema localmente:

1. Clone o repositório:

   git clone https://github.com/seu-usuario/gestao-condominio.git

2. Instale as dependências necessárias (no caso de Tkinter):

   pip install tk

3. Execute o arquivo principal main.py:

   python main.py

## Sobre o envio de notificações por e-mail

O script mailer.py, permite o envio de notificações por e-mail usando o Gmail. 
Ele utiliza a biblioteca smtplib para a comunicação com o servidor SMTP do Gmail e email.mime para formatar as mensagens.

✔ Função Principal:

send_notification(to_email, subject, message): Envia um e-mail para o endereço especificado, com um assunto e uma mensagem personalizados.

✔ Configurações:

O e-mail remetente é definido como exemplo.enviar@gmail.com, e a senha deve ser substituída por uma variável segura (nunca inclua senhas diretamente no código).

Observação:

✔ Para que o envio funcione, é necessário que a opção "Permitir aplicativos menos seguros" esteja ativada na conta do Gmail utilizada.

## Screenshots

Atualizar imagens

##Contribuições ❤️

Contribuições são bem-vindas! Se você deseja contribuir com melhorias ou novos recursos, faça um fork deste repositório, 
crie uma branch para a sua funcionalidade e abra um Pull Request.

1. Faça o fork do projeto.
2. Crie uma nova branch: git checkout -b minha-feature.
3. Faça suas modificações e commit: git commit -m 'Minha nova feature'.
4. Faça o push da sua branch: git push origin minha-feature.
5. Abra um Pull Request.

## Licença  👍

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.


