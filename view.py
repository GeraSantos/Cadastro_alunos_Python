# importando SQLite
import sqlite3 as lite
from datetime import datetime
from tkinter import ttk, messagebox

# criando conexao
try:
    con = lite.connect('Cadastro_alunos.db')
    print("Conexão com banco de dados realizado com sucesso!")
except lite.Error as e:
    print("Erro ao conectar com banco de dados:", e)

# tabela de cursos -------------------------------------------
# criar função criar cursos ( inserir cliente C ) CRUD
def criar_modalidade(i): # criar_cursos
    with con:
        cur = con.cursor()
        query = "INSERT INTO Modalidades (nome, periodo, mensalidade) VALUES (?,?,?)"
        cur.execute(query,i)

#criar_curso(['Java','Duas Semanas', 70])

# Ver todos os cursos (selecionar R) CRUD
def ver_modalidades(): # ver_cursos
    lista = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Modalidades")
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

print(ver_modalidades())

# Atualizar os Cursos (Update U)
def atualizar_modalidade(i): # atualizar
    with con:
        cur = con.cursor()
        query = "UPDATE Modalidades SET nome=?, periodo=?, mensalidade=? WHERE id=?"
        cur.execute(query,i)

#atualizar_modalidade(l)


# Deletar os modalidade (DELETE D)
def deletar_modalidade(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Modalidades WHERE id=?"
        cur.execute(query,i)

deletar_modalidade([1])

# Tabelas de Turmas -------------------------------------------

# Criar turmas ( Inserir C)
def criar_turma(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Turmas (nome, curso, data) VALUES (?,?,?)"
        cur.execute(query,i)

# Ver todas as Turmas ( Read R)
def ver_turmas():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Turmas")
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista
#print(ver_turmas())

# Atualizar as Turmas (Update U)
def atualizar_turmas(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Turmas SET nome=?, curso=?, data=? WHERE id=?"
        cur.execute(query,i)

#atualizar_curso(l)

# Deletar as Turmas (DELETE D)
def deletar_turma(i):
    cur = con.cursor()
    query = "DELETE FROM Turmas WHERE id=?"
    cur.execute(query,i)

#deletar_curso([1])

# Tabelas de Alunos -------------------------------------------
# Criar alunos ( Inserir C)
def criar_alunos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Alunos (nome, email, sexo, data_nascimento, imagem, turma_nome, faixa, grau, telefone, cpf) VALUES (?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query,i)

# Ver todas as Alunos ( Read R)
def ver_alunos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Alunos")
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista
#print(ver_alunos())

# Atualizar as Alunos (Update U)
def atualizar_alunos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Alunos SET nome=?, email=?, sexo=?, data_nascimento=?, imagem=?, turma_nome=?, faixa=?, grau=?, telefone=?, cpf=? WHERE id=?"
        cur.execute(query,i)

#atualizar_alunos(l)

# Deletar as Alunos (DELETE D)
def deletar_alunos(i):
    cur = con.cursor()
    query = "DELETE FROM Alunos WHERE id=?"
    cur.execute(query,i)


# Função para registrar a presença
def get_alunos():
    # Conexão com o banco de dados
    con = lite.connect('Cadastro_alunos.db')
    cur = con.cursor()
    cur.execute("SELECT id, nome FROM Alunos")    
    alunos = cur.fetchall()
    con.close()
    return alunos

