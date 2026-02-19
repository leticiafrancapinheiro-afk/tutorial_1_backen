from flask import Flask, jsonify

app = Flask(__name__)

# Rota inicial
@app.route('/')
def home():
    return "<h1>Servidor Online!</h1><p>Bem-vindo ao Backend.</p>"

# Rota com parâmetro
@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f"Ola, {nome}! Voce acessou uma rota dinamica."

# Rota lista de produtos
@app.route('/produtos')
def listar_produtos():
    itens = ['Teclado', 'Mouse', 'Monitor', 'Cadeira Gamer']
    html = "<h2>Lista de Produtos</h2><ul>"
    for i in itens:
        html += f"<li>{i}</li>"
    html += "</ul>"
    return html

# Rota somar números
@app.route('/somar/<int:v1>/<int:v2>')
def somar(v1, v2):
    res = v1 + v2
    return f"O resultado da soma e: {res}"

# API JSON
@app.route('/api/status')
def status_api():
    dados = {
        "servidor": "HSC Core",
        "status": "Operacional",
        "temperatura_cpu": 45.8,
        "usuarios_online": 12
    }
    return jsonify(dados)

# Rodar servidor
if __name__ == '__main__':
    app.run(debug=True)
