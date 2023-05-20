# api-rest-flask

Uma API REST (Representational State Transfer) é uma interface de programação de aplicações (API) que utiliza o protocolo HTTP para se comunicar com outras aplicações  (GET, POST, PUT, DELETE, etc.).

Esta API foi feita com auxílio do framework Flask do Python, e possibilita o cadastro de pessoas em um banco de dados. A primeira versão dessa API conta com um "banco de dados" simulado em formato de lista em Python. Para operá-la, foi utilizada a ferramenta Postman, onde é possível enviar requisições HTTP para uma API e visualizar as respostas recebidas.

> Status: Em construção :wrench:

## Execução

Para executar essa API, é necessário a instalação do Flask, que pode ser feita através do terminal dentro do venv com o seguinte comando:

```sh
pip install flask
```

Com o Flask instalado é possível executar o código, que estará rodando localmente no seguinte endereço:

http://127.0.0.1:5000

A visualização pode ser feita criando uma API Request no Postman e utilizando o seguinte endereço:

http://127.0.0.1:5000/pessoas

A operação GET possibilitará a visualização do banco de dados:

```sh
{
    "dados": [
        {
            "id": 1,
            "idade": 19,
            "nome": "Fabricio"
        },
        {
            "id": 2,
            "idade": 26,
            "nome": "Juliana"
        },
        {
            "id": 3,
            "idade": 22,
            "nome": "Luan"
        },
        {
            "id": 4,
            "idade": 28,
            "nome": "Mariana"
        },
        {
            "id": 5,
            "idade": 38,
            "nome": "Carlos"
        }
    ],
    "mensagem": "Lista de Pessoas:"
}
```

Já a operação POST possibilitará a inserção de dados. basta colocar o dado dentro do espaço Body, utilizando raw e no formato JSON (JavaScript Object Notation). Veja o seguinte exemplo:

```sh
{
    "id": 6,
    "nome": "Rogério",
    "idade": 57
}
```

Para visualizar o dado inserido, basta realizar a operação GET novamente.

```sh
{
    "dados": [
        {
            "id": 1,
            "idade": 19,
            "nome": "Fabricio"
        },
        {
            "id": 2,
            "idade": 26,
            "nome": "Juliana"
        },
        {
            "id": 3,
            "idade": 22,
            "nome": "Luan"
        },
        {
            "id": 4,
            "idade": 28,
            "nome": "Mariana"
        },
        {
            "id": 5,
            "idade": 38,
            "nome": "Carlos"
        },
        {
            "id": 6,
            "idade": 57,
            "nome": "Rogério"
        }
    ],
    "mensagem": "Lista de Pessoas:"
}
```

Porém, utilizar o programa dessa forma tem um problema. Assim que reiniciá-lo, as informações adicionadas são perdidas. Por isso, existe a necessidade de um banco de dados para armazenamento dessas informações.

## Banco de dados

O banco de dados foi criado com auxílio da biblioteca SQL Alchemy.