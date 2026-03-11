#Imports do flask, render template que é para fazer o web, o sqlalchemy que é para fazer a modelagem dos dados
# e o 'os' que é para gerenciar os arquivos do seu repositorio
from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy
import os 

#Instanciando o Flask 
app = Flask(__name__)

#Definindo o endereço do banco 
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:nuvem123@db:5432/projeto_db "

#Instanciando o sqlalchemy para que possa criar tabelas e etc..
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(150), nullable = False)
    cpf = db.Column(db.String(11), unique=True, nullable=False )
    email = db.Column(db.String(255), nullable=False)
    senha = db.Column (db.String(20), nullable=False)


@app.route('/')
def consulta_usuarios():
    try:
        #Fazendo uma busca de todos os usuários
        usuarios = Usuario.query.all()

        html = """
        <h1>--- Lista de Usuários ---</h1>
        <table border="1">
            <tr>
                <th>ID</th><th>Nome</th><th>CPF</th><th>Email</th>
            </tr>
            {% for u in usuarios %}S
            <tr>    
                <td>{{ u.id }}</td>
                <td>{{ u.nome }}</td>
                <td>{{ u.cpf }}</td>
                <td>{{ u.email }}</td>
            </tr>
            {% endfor %}
        </table>
        """
        return render_template_string(html, usuarios=usuarios)
    except Exception as e:
        return f"<h1>Erro ao consultar o banco:</h1><p>{str(e)}</p>"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)