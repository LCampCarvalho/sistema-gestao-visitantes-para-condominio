import sqlite3


# Função para criar o banco de dados e as tabelas
def create_db():
    conn = sqlite3.connect('gestao_condominio.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS visitantes (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT,
                 cpf TEXT,
                 apartamento TEXT,
                 data_visita TEXT,
                 hora_entrada TEXT,
                 hora_saida TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS veiculos (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 placa TEXT,
                 modelo TEXT,
                 cor TEXT,
                 apartamento TEXT,
                 hora_entrada TEXT,
                 hora_saida TEXT)''')
    conn.commit()
    conn.close()


# Função para adicionar visitante
def add_visitante(nome, cpf, apartamento, data_visita, hora_entrada):
    conn = sqlite3.connect('gestao_condominio.db')
    c = conn.cursor()
    c.execute('INSERT INTO visitantes (nome, cpf, apartamento, data_visita, hora_entrada) VALUES (?, ?, ?, ?, ?)',
              (nome, cpf, apartamento, data_visita, hora_entrada))
    conn.commit()
    conn.close()


# Função para adicionar veículo
def add_veiculo(placa, modelo, cor, apartamento, hora_entrada):
    conn = sqlite3.connect('gestao_condominio.db')
    c = conn.cursor()
    c.execute('INSERT INTO veiculos (placa, modelo, cor, apartamento, hora_entrada) VALUES (?, ?, ?, ?, ?)',
              (placa, modelo, cor, apartamento, hora_entrada))
    conn.commit()
    conn.close()


# Função para obter todos os visitantes
def get_visitantes():
    conn = sqlite3.connect('gestao_condominio.db')
    c = conn.cursor()
    c.execute('SELECT * FROM visitantes')
    visitantes = c.fetchall()
    conn.close()
    return visitantes


# Função para obter todos os veículos
def get_veiculos():
    conn = sqlite3.connect('gestao_condominio.db')
    c = conn.cursor()
    c.execute('SELECT * FROM veiculos')
    veiculos = c.fetchall()
    conn.close()
    return veiculos


# Função para registrar saída de visitante
def registrar_saida_visitante(cpf, hora_saida):
    conn = sqlite3.connect('gestao_condominio.db')
    c = conn.cursor()
    c.execute('UPDATE visitantes SET hora_saida = ? WHERE cpf = ? AND hora_saida IS NULL', (hora_saida, cpf))
    conn.commit()
    conn.close()


# Função para registrar saída de veículo
def registrar_saida_veiculo(placa, hora_saida):
    conn = sqlite3.connect('gestao_condominio.db')
    c = conn.cursor()
    c.execute('UPDATE veiculos SET hora_saida = ? WHERE placa = ? AND hora_saida IS NULL', (hora_saida, placa))
    conn.commit()
    conn.close()


# Função para obter visitantes presentes (sem saída registrada)
def get_visitantes_presentes():
    conn = sqlite3.connect('gestao_condominio.db')
    c = conn.cursor()
    c.execute('SELECT * FROM visitantes WHERE hora_saida IS NULL')
    visitantes = c.fetchall()
    conn.close()
    return visitantes


# Função para obter veículos presentes (sem saída registrada)
def get_veiculos_presentes():
    conn = sqlite3.connect('gestao_condominio.db')
    c = conn.cursor()
    c.execute('SELECT * FROM veiculos WHERE hora_saida IS NULL')
    veiculos = c.fetchall()
    conn.close()
    return veiculos

# Função para excluir um visitante pelo CPF
def excluir_registro_visitante(cpf):
    conn = sqlite3.connect('gestao_condominio.db')
    c = conn.cursor()
    c.execute('DELETE FROM visitantes WHERE cpf = ?', (cpf,))
    conn.commit()
    conn.close()

# Função para excluir um veículo pela placa
def excluir_registro_veiculo(placa):
    conn = sqlite3.connect('gestao_condominio.db')
    c = conn.cursor()
    c.execute('DELETE FROM veiculos WHERE placa = ?', (placa,))
    conn.commit()
    conn.close()
