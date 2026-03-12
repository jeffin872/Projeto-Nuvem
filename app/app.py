#Imports do flask, render template que é para fazer o web, o sqlalchemy que é para fazer a modelagem dos dados
# e o 'os' que é para gerenciar os arquivos do seu repositorio
from flask import Flask, render_template_string, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os 

#Instanciando o Flask 
app = Flask(__name__)

#Definindo o endereço do banco 
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:nuvem123@db:5432/projeto_db"

#Instanciando o sqlalchemy para que possa criar tabelas e etc..
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(150), nullable = False)
    cpf = db.Column(db.String(11), unique=True, nullable=False )
    email = db.Column(db.String(255), nullable=False)
    senha = db.Column (db.String(20), nullable=False)



#aqui eu fiz um html simples que mostra a lista de usuário por meio de um for 
#usei os metodos get e post, para adicionar usuário por meio de um form, fica melhor de mostrar o funcionamento 
@app.route('/', methods=['GET', 'POST'])
def consulta_usuarios():
    try:
        if request.method == 'POST':
            #Pegando os dados do formulário e colocando num objeto que sera uma nova coluna da tabela
            novo_usuario = Usuario(
                nome=request.form['nome'],
                cpf=request.form['cpf'],
                email=request.form['email'],
                senha=request.form['senha']
            )
            #aqui eu vou fazer o commit do novo usuário no banco de dados, como se fosse o git, faço o add e depois o commit
            db.session.add(novo_usuario)
            db.session.commit()

            #o redirect manda o usuário de volta pra mesma pagina, um refresh pra atualizar o dado auomatico
            #o url_for é pra mostrar qual a rota que eu quero mandar (que é a mesma)
            return redirect(url_for('consulta_usuarios')) 


        #Fazendo uma busca de todos os usuários
        usuarios = Usuario.query.all()

        return render_template_string('''
            <!DOCTYPE html>
            <html lang="pt-br">        
            <head>                      
                <meta charset="UTF-8">
                <title>Usuários</title>               
                <style>
                    form {
                        width: 300px;
                        margin-top: 10px;
                    }

                    label {
                        display: block;
                        margin-top: 10px;
                    }

                    input {
                        width: 100%;
                        padding: 5px;
                        margin-top: 3px;
                    }

                    button {
                        margin-top: 10px;
                        padding: 6px 10px;
                    }
                </style>              
            </head>                
            <body>  
                <h1>--- Lista de Usuários ---</h1>
                <table border="1" style="margin-bottom: 10px;">
                    <tr>
                        <th>ID</th><th>Nome</th><th>CPF</th><th>Email</th>
                    </tr>
                    {% for u in usuarios %}
                    <tr>    
                        <td>{{ u.id }}</td>
                        <td>{{ u.nome }}</td>
                        <td>{{ u.cpf }}</td>
                        <td>{{ u.email }}</td>
                    </tr>
                    {% endfor %}
                </table>
                                      
                <h2> Cadastrar novo usuário: </h2>
                <form method='POST' > 
                    <label>Nome</label>
                    <input type="text" name="nome" required>

                    <label>CPF</label>
                    <input type="text" name="cpf" required>

                    <label>Email</label>
                    <input type="email" name="email" required>

                    <label>Senha</label>
                    <input type="password" name="senha" required>
                                      
                    <button type="submit"> Cadastrar</button>
                                      
                </form>
                                      
            </body>
            </html>                                
        ''', usuarios=usuarios)

    except Exception as e:
        return f"<h1>Erro ao consultar o banco:</h1><p>{str(e)}</p>"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)