import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('database/crm.db')
cursor = conn.cursor()

# Tabela de contatos
cursor.execute('''
CREATE TABLE IF NOT EXISTS contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL UNIQUE,
    status TEXT DEFAULT 'Novo',
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);
''')

# Tabela de mensagens
cursor.execute('''
CREATE TABLE IF NOT EXISTS mensagens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contato_id INTEGER,
    mensagem TEXT NOT NULL,
    enviado BOOLEAN DEFAULT 0,
    enviado_em DATETIME,
    FOREIGN KEY (contato_id) REFERENCES contatos (id)
);
''')

conn.commit()
conn.close()
print("Banco de dados configurado!")
