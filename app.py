from flask import Flask, render_template, request, redirect, url_for, jsonify
from whatsapp_client import WhatsAppClient  # Biblioteca para QR Code (Exemplo)
import sqlite3

app = Flask(__name__)

# Conexão com o banco
def get_db_connection():
    conn = sqlite3.connect('database/crm.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contatos', methods=['GET', 'POST'])
def whatsapp():
    qr_code = client.get_qr_code()
    return render_template('whatsapp.html', qr_code=qr_code)

def contatos():
    conn = get_db_connection()
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        conn.execute('INSERT INTO contatos (nome, telefone) VALUES (?, ?)', (nome, telefone))
        conn.commit()
        conn.close()
        return redirect(url_for('contatos'))
    
    contatos = conn.execute('SELECT * FROM contatos').fetchall()
    conn.close()
    return render_template('contatos.html', contatos=contatos)

if __name__ == '__main__':
    app.run(debug=True)
