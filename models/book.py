#CONTEM OS MODELOS QUE REPRESENTAM AS ENTIDADES DO BANCO
#BOOK REPRESENTA A ENTIDADE BOOK
from uuid import uuid4


from sqlalchemy import String, TEXT
from sqlalchemy.dialects.postgresql import UUID

from db import db

class book(db.models):
#INDICAR QUE BOOK É UM MODELO GERENCIADO PEL SQLALCHEMY
    __tablename__ = 'book'
    #DEFINE O NOME DA TABELA 

    ID = db.column(
        UUID(as_uuid=True), #vou usar o UUID
        primary_key = True, # chave primaria
        default = uuid4 #quando criar um novo livro, um UUID sera criado
    )
    #titulo
    title = db.Column(
        String(255), # recebe a string
        nullable = False # nao aceita nulo
    )

    author = db.Column(
        String(255),nullable = False   
    )

    description  = db.Column(
        TEXT, #textos maiores
        nullable = False
    )

    is_favorite  =  db.Column(
    db.Boolean,
    nullable = False,
    default = False
    )

    is_reading = db.Column(
        db.Boolean,
        nullable = False,
        default = False
    )

    is_finishing = db.Column(
        db.Boolean,
        nullable = False,
        default = False
    )

 #Transformando o modelo em dicionario

"""
POR ISSO SERA CRIADO UM METODO RESPONSAVL POR TRANSFORMAR
O OBJETO BOOK EM UM DICIONARIO PYTHON

QUANDO OCORRER UMA CNSULTA AO NOSSO SISTEMA ELE RETORNA UM OBJETO BOOK,
ELE NÃO É SIMPLESMENTE UM DICT PYTHON.
O MÉTODO AS_DICT() VAI FUNCIONAR COMO UMA CAMADA D CONVERSÃO, SELECIONANDO APENAS O 
NECESSRIO PARA SER EXPOSTO NO APII  TRANSFORMANDO EM UM DCIT
ESTRUTURA QUE PODE SER FACILMENTE SERALIZADA PARA JSONNA RESPOSTA HTTP

"""
def as_dict(self):
    return{
        'id': str(self.id), #necessario conversao forçada
        'author': self.author,
        'description': self.description,
        'is_favorite': self.is_favorite,
        'is_reading': self.is_reading,
        'is_finishing': self.is_finishing

    }