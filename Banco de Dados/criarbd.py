#importando sqlite3
import sqlite3

# criando conexao
try:
    con = sqlite3.connect('Cadastro_alunos.db')
    print("Conexão com banco de dados realizado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao conectar com banco de dados:", e)

# Criando tabela de modalidade
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS Modalidades(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            periodo TEXT,
            mensalidade REAL     
        )""")
        
        print("tabela modalidade criado com sucesso!")

except sqlite3.Error as e:
    print("Erro ao criar tabela de modalidades:", e)

# Criando tabela de turmas
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS Turmas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cursos TEXT,
            data DATE,
            FOREIGN KEY (cursos) REFERENCES  curso (c_curso) ON UPDATE CASCADE ON DELETE CASCADE   
        )""")
        
        print("tabela turmas criada com sucesso!")
        
except sqlite3.Error as e:
    print("Erro ao criar tabela de turmas:", e)


# Criando tabela de alunos
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            telefone TEXT,
            sexo TEXT,
            imagem TEXT,
            data_nascimento DATE,
            faixa TEXT,
            grau TEXT,
            turma_nome TEXT,
            FOREIGN KEY (turma_nome) REFERENCES  turmas (nome) ON DELETE CASCADE   
        )""")
        
        print("tabela alunos criada com sucesso!")
        
except sqlite3.Error as e:
    print("Erro ao criar tabela de alunos:", e)