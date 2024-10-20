# Solidarize - Solidariedade em Rede  

O Solidarize é uma plataforma de voluntariado que conecta ONGs e projetos sociais com voluntários interessados em fazer a diferença. O aplicativo facilita a inscrição em oportunidades de voluntariado, o gerenciamento de perfis de usuários e organizações, além de oferecer funcionalidades de avaliação e emissão de certificados para os participantes.

## Visão do Projeto  

O Solidarize visa englobar a comunidade local, promovendo o voluntariado acessível e eficiente. Nosso objetivo é ajudar ONGs a encontrarem voluntários engajados e facilitar para os voluntários a busca por oportunidades que correspondam aos seus interesses e disponibilidade.

## Funcionalidades Principais  

- Registro de Usuários: Voluntários e organizações podem se registrar na plataforma, com verificação de email e segurança reforçada.  
- Sistema de Oportunidades: ONGs podem criar e gerenciar oportunidades de voluntariado, e voluntários podem se inscrever facilmente.  
- Painel Administrativo: Gestão eficiente de usuários, ONGs e oportunidades através de um painel exclusivo para administradores.  
- Avaliação Mútua: Tanto o voluntário quanto a ONG podem ser avaliados, promovendo uma cultura de responsabilidade e qualidade.  
- Certificação: Emissão automática de certificados de participação para os voluntários que concluírem suas atividades.  

## Tecnologias Utilizadas  

+ Backend: Django - Framework web Python.
+ Frontend: HTML, CSS, JavaScript.
+ Banco de Dados: PostgreSQL.
+ Autenticação e Autorização: Sistema de usuários do Django, com integração para autenticação via Google.
+ Emails: Configuração de envio de emails com SMTP para verificação e confirmação de contas.

# Instalação e Configuração  

## Pré-requisitos

Certifique-se de ter instalado:

[Python](https://www.python.org/downloads/)  
[PostgreSQL](https://www.postgresql.org/download/)  
Virtualenv ` pip install virtualenv `  

## Passos para instalação

Clone o repositório:

```sh
git clone https://github.com/seu-usuario/solidarize.git
```

Crie e ative um ambiente virtual:

```sh
python -m venv venv
source venv/bin/activate  # Para Windows: venv\Scripts\activate
```

Instale as dependências:

```sh
pip install -r requirements.txt
```

## Configure o banco de dados:

Crie um banco de dados no PostgreSQL.

Atualize o arquivo settings.py com as credenciais do banco de dados.

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Realize as migrações do banco de dados:

```sh
python manage.py migrate
```

Crie um superusuário:

```sh
python manage.py createsuperuser
```

Inicie o servidor local:

```sh
python manage.py runserver
```

Acesse a plataforma: Abra o navegador e vá para http://127.0.0.1:8000.

# Contribuindo

Se você deseja contribuir para o Solidarize, siga os passos abaixo:

## Faça um fork do projeto.

Crie uma branch para sua feature:
```sh
git checkout -b minha-feature
```

Realize o commit das suas alterações:
```sh
git commit -m 'Adiciona nova funcionalidade'
```

Faça o push para a branch:
```sh
git push origin minha-feature
```

Abra um pull request e descreva suas mudanças.

# Metodologia

O desenvolvimento do projeto segue a metodologia ágil Scrum, com a realização de Sprints para planejar e implementar novas funcionalidades de forma colaborativa e iterativa. O objetivo é manter o ciclo de feedback constante e garantir a entrega contínua de valor.

## Sprints  

- Sprint 1: Registro de Usuários e Validação de Email.  
- Sprint 2: Sistema de Gerenciamento de Oportunidades e Perfis de Voluntários e ONGs.  
- Sprint 3: Sistema para validar a participação do voluntário através do GPS.  
- Sprint 4: Sistema de Avaliação e Certificação de Voluntários.  
- Sprint 5: Melhorias no Painel Administrativo.

## Licença   

Este projeto está licenciado sob os termos da MIT License.  

## Contato  

*Para dúvidas ou sugestões, entre em contato:*

Nome: Ericson Schmidt Bicalho  
Email: schcodes@gmail.com  
LinkedIn: [Ericson Schmidt](https://www.linkedin.com/in/ericson-schmidt-bicalho/)  

Nome: Nicolas Gabriel de Oliveira  
Email: nicolassg121@gmail.com  
LinkedIn: [Nicolas Gabriel](https://www.linkedin.com/in/nicolasgbo/)  
