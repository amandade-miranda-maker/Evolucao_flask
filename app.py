#responsavel pela aplicacao do flask
#e pelo epints
#app de gerenciamento de livros
#consultar livros
#editar
#atualizar
#deletar
#favoitar
#livros em leitura
#livros finalizados
import os
from dotenv import load_dotenv
from flask import Flask
from db import db
load_dotenv()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URL"] = os.getenv('DATABASE_URL')
print(os.getenv("DATABASE_URL"))

