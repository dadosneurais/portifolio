from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client['portifolio']
contatos_collection = db.portifolio

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Requerido para o uso de flash

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/curriculo')
def curriculo():
    return render_template('curriculo.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']
        
        contato_data = {
            'nome': nome,
            'email': email,
            'assunto': assunto,
            'mensagem': mensagem
        }
        
        contatos_collection.insert_one(contato_data)
        flash('Mensagem enviada com sucesso!')
        return redirect(url_for('contato'))

    return render_template('contato.html')

@app.route('/ajuda')
def ajuda():
    return render_template('ajuda.html')

if __name__ == '__main__':
    app.run(debug=True)
