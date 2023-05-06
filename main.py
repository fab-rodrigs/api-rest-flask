from flask import Flask, make_response, jsonify, request
from bd import Pessoas # importa lista

app = Flask(__name__) # define nome do app
app.config['JSON_SORT_KEYS'] = False # desativa a ordenação em ordem alfabética

@app.route('/pessoas', methods=['GET']) # decorator para o método GET
def get_pessoas():
    return make_response( # formatação
        jsonify(
            mensagem = 'Lista de Pessoas:',
            dados = Pessoas
        )
    )



@app.route('/pessoas', methods=['POST']) # decorator para o método POST
def create_pessoa():
    pessoa = request.json # recebe pessoa
    Pessoas.append(pessoa) # anexa pessoa na lista
    return make_response( # formatação
        jsonify(
            mensagem = 'Pessoa cadastrada com sucesso!',
            pessoa = pessoa
        )
    )
    

app.run() # roda app