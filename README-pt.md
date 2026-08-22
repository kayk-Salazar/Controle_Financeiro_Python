#  Bank System Simulator

Um sistema bancário desenvolvido em **Python** com o objetivo de simular operações bancárias básicas, aplicando conceitos de **Programação Orientada a Objetos (POO)**, separação de responsabilidades, arquitetura em camadas e integração com banco de dados PostgreSQL.

O projeto foi desenvolvido como um projeto de portfólio, buscando representar uma aplicação bancária de forma organizada e próxima de uma estrutura utilizada em projetos reais.

> **Status:** MVP funcional em desenvolvimento.

---

##  Sobre o projeto

O **Bank Simulator** simula o funcionamento básico de um sistema bancário, permitindo o cadastro e autenticação de usuários, gerenciamento de contas, operações financeiras e consulta de transações.

O sistema possui dois fluxos principais:

*  Usuário
*  Administrador

A aplicação atualmente possui uma interface executada pelo terminal (CLI).

O projeto está sendo desenvolvido de forma incremental. Algumas funcionalidades já estão implementadas e funcionando através da interface, enquanto outros métodos e recursos já estruturados no código serão implementados em versões futuras.

---

##  Funcionalidades

###  Usuário

O usuário pode:

* Criar uma conta de usuário
* Realizar login utilizando CPF e senha
* Visualizar seus dados pessoais
* Visualizar os dados da sua conta bancária
* Consultar saldo
* Realizar depósitos
* Realizar saques
* Consultar extratos
* Consultar extratos dos últimos 30 dias
* Consultar extratos dos últimos 90 dias
* Consultar apenas depósitos
* Consultar apenas saques
* Consultar todas as transações
* Encerrar a sessão

Durante o cadastro são realizadas validações dos dados informados, incluindo:

* Nome
* Sobrenome
* CPF
* Data de nascimento
* E-mail
* Telefone
* Senha

A senha também possui regras de validação relacionadas ao tamanho, letras maiúsculas, números e caracteres especiais.

---

###  Administrador

O administrador possui funcionalidades voltadas para consulta e gerenciamento dos registros do sistema.

Atualmente, o menu administrativo possui três áreas principais:

* Usuários
* Contas
* Transações

####  Busca de usuários

O administrador pode buscar usuários individualmente por:

* ID
* CPF
* E-mail
* Telefone

Após localizar um usuário, o sistema permite visualizar uma prévia e entrar nos detalhes do usuário.

Nos detalhes, é possível visualizar:

* Dados pessoais
* ID do usuário
* Conta vinculada
* Número da conta
* Saldo
* Status da conta
* Data de criação

Também é possível:

* Ativar uma conta
* Bloquear uma conta
* Consultar transações do usuário
* Voltar ao menu anterior

---

### 🏦 Busca de contas

O administrador pode consultar contas por:

* ID
* Número da conta
* Contas ativas
* Contas bloqueadas

As buscas por ID e número da conta retornam uma conta específica.

As buscas por status permitem consultar várias contas simultaneamente.

---

###  Consulta de transações

O administrador também possui acesso às consultas globais de transações.

É possível consultar:

* Transações dos últimos 30 dias
* Transações dos últimos 90 dias
* Depósitos
* Saques
* Todas as transações

---

##  Arquitetura

O projeto utiliza uma arquitetura organizada em camadas, buscando separar as responsabilidades de cada parte da aplicação.

Estrutura principal:

```text
bank-simulator/
│
├── database/
│   ├── connection.py
│   └── initializer.py
│
├── entities/
│
├── exceptions/
│   └── custom_exceptions.py
│
├── repositories/
│
├── security/
│   └── password_hash.py
│
├── services/
│
├── ui/
│   ├── main_ui.py
│   ├── user_ui.py
│   └── admin_ui.py
│
├── validators/
│
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

### Responsabilidade das camadas

**Database**

Responsável pela conexão com o PostgreSQL e inicialização das tabelas.

**Entities**

Representam as entidades utilizadas pelo sistema.

**Repositories**

Responsáveis pelo acesso e manipulação dos dados no banco de dados.

**Services**

Concentram as regras de negócio da aplicação.

**Validators**

Responsáveis pela validação das entradas e regras específicas dos dados.

**Security**

Responsável por recursos relacionados à segurança, como o hash das senhas.

**UI**

Responsável pela interação com o usuário através do terminal.

**Exceptions**

Contém as exceções personalizadas utilizadas pela aplicação.

---

##  Banco de dados

O projeto utiliza **PostgreSQL** como banco de dados.

O MVP possui entidades relacionadas a:

* Usuários
* Contas
* Transações

A relação principal pode ser representada da seguinte forma:

```text
USER
 │
 │ 1
 │
 │ 1
 ▼
ACCOUNT
 │
 │ 1
 │
 │ N
 ▼
TRANSACTION
```

Um usuário possui uma conta e uma conta pode possuir várias transações.

---

##  Segurança

As senhas dos usuários não são armazenadas diretamente no banco de dados.

O projeto utiliza **bcrypt** para gerar o hash das senhas antes do armazenamento.

As informações de conexão com o banco de dados também são mantidas através de variáveis de ambiente.

Dados sensíveis, como senha do PostgreSQL, não devem ser enviados para o GitHub.

---

##  Tecnologias utilizadas

* **Python**
* **PostgreSQL**
* **Psycopg**
* **bcrypt**
* **python-dotenv**
* **validate-docbr**
* **email-validator**
* **phonenumbers**

Também são utilizados recursos nativos do Python, como:

* `datetime`
* `decimal`
* `re`

---

##  Instalação

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre na pasta do projeto:

```bash
cd bank-simulator
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual.

No Windows:

```bash
.venv\Scripts\activate
```

### 3. Instale as dependências

Com o ambiente virtual ativado:

```bash
pip install -r requirements.txt
```

---

## 🗄️ Configuração do PostgreSQL

O projeto utiliza um banco PostgreSQL local.

Primeiro, crie um banco de dados PostgreSQL para o projeto.

Depois, configure as variáveis de ambiente.

Crie um arquivo chamado:

```text
.env
```

Esse arquivo deve conter as informações de conexão do seu ambiente local.

Exemplo:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=bank_system
DB_USER=postgres
DB_PASSWORD=sua_senha
```

> **Importante:** o arquivo `.env` não deve ser enviado para o GitHub, pois pode conter informações sensíveis.

O projeto disponibiliza um arquivo `.env.example` contendo apenas a estrutura necessária para configuração.

---

## ▶ Executando o projeto

Depois de configurar o ambiente virtual, instalar as dependências e configurar o PostgreSQL, execute o arquivo principal:

```bash
python main.py
```

O `main.py` é responsável por inicializar os componentes da aplicação, estabelecer a conexão com o banco de dados, inicializar as tabelas e iniciar a interface principal do sistema.

---

##  Estado atual do projeto

Este projeto está atualmente em sua versão **MVP (Minimum Viable Product)**.

O fluxo principal da aplicação já está funcional, incluindo:

* Cadastro
* Login
* Validação de dados
* Criação e consulta de contas
* Depósitos
* Saques
* Consulta de saldo
* Consulta de transações
* Busca administrativa
* Consulta de usuários
* Consulta de contas
* Bloqueio e ativação de contas

Entretanto, alguns métodos e estruturas já presentes no projeto ainda não estão totalmente integrados à interface.

Isso faz parte do desenvolvimento incremental do projeto.

---

##  Próximos passos

Algumas funcionalidades planejadas para futuras versões incluem:

* Implementar autenticação específica para administradores
* Integrar completamente o bloqueio de contas às operações bancárias
* Permitir que o administrador entre e gerencie contas retornadas em buscas globais
* Expandir as funcionalidades administrativas
* Melhorar a interface do terminal
* Adicionar testes automatizados
* Melhorar o tratamento de erros
* Expandir as consultas e filtros administrativos
* Evoluir a arquitetura conforme a complexidade do sistema aumentar

---

##  Objetivo do projeto

O principal objetivo do **Bank Simulator** é servir como projeto de estudo e portfólio, demonstrando conhecimentos em:

* Python
* Programação Orientada a Objetos
* SQL
* PostgreSQL
* Arquitetura em camadas
* Separação de responsabilidades
* Padrão Repository
* Regras de negócio
* Validação de dados
* Tratamento de exceções
* Segurança de senhas
* Git e GitHub

O projeto também representa uma evolução contínua dos conhecimentos adquiridos durante o desenvolvimento.

---

##  Desenvolvimento

Projeto desenvolvido para fins de estudo, prática e portfólio profissional.

O sistema continuará sendo evoluído conforme novos conhecimentos e funcionalidades forem incorporados.
