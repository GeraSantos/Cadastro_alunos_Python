#importando sqlite3
import sqlite3

# criando conexao
try:
    con = sqlite3.connect('Cadastro_alunos.db')
    print("Conexão com banco de dados realizado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao conectar com banco de dados:", e)

# Criando tabela de cursos
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS cursos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
            duracao TEXT,
            preco REAL     
            )""")
        
        print("tabela cursos criado com sucesso!")

except sqlite3.Error as e:
    print("Erro ao criar tabela de cursos:", e)

# Criando tabela de turmas
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS turmas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            curso_nome TEXT,
            data_inicio DATE,
            FOREIGN KEY (curso_nome) REFERENCES  cursos (nome) ON UPDATE CASCADE ON DELETE CASCADE   
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
            alunos TEXT,
            data_inicio DATE,
            FOREIGN KEY (alunos) REFERENCES  alunos (nome) ON UPDATE CASCADE ON DELETE CASCADE   
            )""")
        
        print("tabela alunos criada com sucesso!")
        
except sqlite3.Error as e:
    print("Erro ao criar tabela de alunos:", e)