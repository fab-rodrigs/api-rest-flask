from flask import Flask, make_response, jsonify, request
from bd import Pessoas # importa lista
import sqlalchemy # banco de dados
from sqlalchemy.orm import declarative_base # declarando mapeamento
from sqlalchemy import Column, Integer, String # Colunas, dados tipo inteiro e strings
from sqlalchemy.orm import sessionmaker

# conexão com banco de dados
engine = sqlalchemy.create_engine('sqlite:///bd.db', echo=True) # Cria arquivo para banco de dados, echo = True possibilita ver o equivalente em SQL

Base = declarative_base()

# Classe para pessoas do banco de dados
class Pessoas(Base):
  __tablename__ = 'pessoas'
  id = Column(Integer, primary_key=True) # chave
  nome = Column(String(50))
  idade = Column(Integer)
  def __repr__(self): # função de formatação
    return "<Pessoas(nome={}, idade={})>".format(self.nome, self.idade)

Base.metadata.create_all(engine) # cria tabela no banco de dados

# Criando uma sessão (conexão entre app e banco de dados)
Session = sessionmaker(bind=engine) # Classe Session como um construtor de sessões

#session.add_all([ # função para adicionar mais de uma pessoa no banco de dados
#    Pessoas(nome='Fabricio', idade = 19),
#    Pessoas(nome='Juliana', idade = 26),
#    Pessoas(nome='Luan', idade = 22),
#    Pessoas(nome='Mariana', idade = 28),
#    Pessoas(nome='Carlos', idade = 38),
#])

# Limpa a tabela Pessoas
# session.query(Pessoas).delete()

#session.commit() # inserindo informações no banco de dados

#for instance in session.query(Pessoas).order_by(Pessoas.id): # imprimindo dados
#  print(instance.nome, instance.idade)

app = Flask(__name__) # define nome do app
app.config['JSON_SORT_KEYS'] = False # desativa a ordenação em ordem alfabética

@app.route('/pessoas', methods=['GET']) # decorator para o método GET
def get_pessoas():
    session = Session() # Instância da sessão real a partir da classe Session
    pessoas = session.query(Pessoas).all()
    session.close()
    
    dados = []
    for pessoa in pessoas:
        dicionario = {'nome': pessoa.nome, 'idade': pessoa.idade}
        dados.append(dicionario)

    return make_response( # formatação
        jsonify(
            mensagem = 'Lista de Pessoas:',
            dados = dados
        )
    )

@app.route('/pessoas', methods=['POST']) # decorator para o método POST
def create_pessoa():
    #session = Session() # Instância da sessão real a partir da classe Session
    pessoa = Pessoas(nome = request.json['nome'], idade = request.json['idade']) # recebe pessoa
    #session.add(pessoa)
    #session.commit()
    #session.close()
    Pessoas.append(pessoa) # anexa pessoa na lista
    return make_response( # formatação
        jsonify(
            mensagem = 'Pessoa cadastrada com sucesso!',
            pessoa={'nome': pessoa.nome, 'idade': pessoa.idade}
        )
    )
if __name__ == '__main__':
    app.run() # roda app