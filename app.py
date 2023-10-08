from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from tkinter import messagebox

app = Flask(__name__)

# Configurações do banco de dados SQL
db_name = "cadastro_db.sqlite"

# Rota para a página de cadastro
@app.route('/')
def cadastro():
    return render_template('projeto.html')

# Rota para o formulário
@app.route('/processar_cadastro', methods=['POST'])
def processar_cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        salario = request.form['salario']
        integrantes = request.form['integrantes']
        menores_de_16 = request.form['menores_de_16']
        numero_de_menores = request.form['numero_de_menores']
        matriculados = request.form['matriculados']

        # Conectar ao banco de dados
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Inserir os dados na tabela
        cursor.execute("INSERT INTO cadastro (nome_completo, cpf, telefone, salario, integrantes, menores_de_16, numero_de_menores, matriculados) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (nome, cpf, telefone, salario, integrantes, menores_de_16, numero_de_menores, matriculados))
        conn.commit()
        conn.close()

        return 'Cadastro realizado com sucesso!'

if __name__ == '__main__':
    # Inicializar Flask
    app.run(debug=True)

