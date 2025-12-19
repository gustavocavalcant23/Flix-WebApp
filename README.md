# Flix-WebApp

O **Flix-WebApp** é uma aplicação web desenvolvida para estudo, que simula uma plataforma de gerenciamento e visualização de filmes.  
O projeto é dividido em **backend** e **frontend**, com uma API responsável por fornecer os dados e uma interface web para consumo dessas informações.

O backend foi desenvolvido com **Django + Django REST Framework**, enquanto o frontend utiliza **Streamlit** para construção da interface.  
O sistema permite o gerenciamento de **filmes, gêneros, atores e reviews**, além de contar com comandos customizados para importação de dados via CSV.


## Estrutura do Projeto

```text
Flix-WebApp/
├── Flix-API/
│       ├──apps 
│       ├──manage.py 
│       ├──actors.csv 
│       ├──genres.csv 
│       ├──movies.csv 
│       └── ... 
│   
├── Flix-APP/
│   ├── apps  
│   ├── app.py
│   └── ...
└── README.md
```


## Instalação e Execução

### Clonar o repositório

```bash
git clone https://github.com/gustavocavalcant23/Flix-WebApp.git
```

O projeto usa **dois terminais**, então teremos um para o backend e outro para o frontend.


## Backend

### Acessando o diretório

````bash
cd Flix-API
````

### Criando e ativando a venv

````bash
python -m venv venv
````

Windows:

````bash
venv\Scripts\activate
````

Linux/Mac:
```` bash
source venv/vin/activate
````

### Instalando dependências

```` bash
pip install -r requirements.txt
````

### Executando migrações

```` bash
python manage.py migrate
````

### Criando SuperUser

```` bash
python manage.py createsuperuser
````

### Importando dados via CSV (opcional)

**Importe na ordem abaixo**:

```` bash
python manage.py import_genres genres.csv

python manage.py import_actors actors.csv

python manage.py import_movies movies.csv
````

### Rodando servidor

```` bash
python manage.py runserver
````
O servidor estará disponível em https://localhost:8000/admin


## Frontend

Em **outro terminal**, faça o seguinte:

### Acessando o diretório

````bash
cd Flix-APP
````

### Criando e ativando a venv

````bash
python -m venv venv
````

Windows

````bash
venv\Scripts\activate
````

Linux/Max
```` bash
source venv/vin/activate
````

### Instalando dependências

```` bash
pip install -r requirements.txt
````

### Rodando aplicação Streamlit

```` bash
streamlit run app.py
````

O servidor estará disponível em https://localhost:8501

## Recomendações

- Crie um terminal para cada parte do sistema.
- Importe os arquivos .csv para melhor experiência.
- Importe os arquivos .csv na ordem recomendada
- Faça login com o username e senha fornecidos na criação do superuser



## Tecnologias Utilizadas

- Python
- Django
- Django Rest Framework (DRF)
- Simple JWT
- Streamlit



## Objetivo do projeto

O Flix-WebApp tem como objetivo o desenvolvimento de uma aplicação web completa, baseada em **arquitetura cliente-servidor**, para gerenciamento e visualização de dados relacionados a filmes.

O projeto foi desenvolvido com foco em:

- Construção de uma **API REST** utilizando **Django** e **Django Rest Framework**

- Implementação de **autenticação e autorização** via JWT, utilizando **SimpleJWT**

- Modelagem de **dados relacionais** envolvendo filmes, gêneros, atores e avaliações

- **Consumo de API** por um frontend desacoplado, desenvolvido com **Streamlit**

- Aplicação de boas práticas de organização de código, com separação de responsabilidades em camadas **(Repository e Service)**

- Implementação de **Django Commands** para **importação** e **exportação** de dados via **CSV**

- **Otimização de performance** no frontend por meio de cache manual com **session_state**

- **Padronização e qualidade** de código utilizando **Flake8** como linter, seguindo rigorosamente as **normas e boas práticas** definidas pela **PEP 8** de Guido Van Rossum

O projeto possui caráter educacional e foi desenvolvido com o objetivo de consolidar conhecimentos em Python, Django, APIs REST, autenticação JWT, Streamlit e arquitetura de software.