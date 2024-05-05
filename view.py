# importando SQLite
import sqlite3 as lite

# criando conexao
try:
    con = lite.connect('Cadastro_alunos.db')
    print("Conexão com banco de dados realizado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao conectar com banco de dados:", e)

# tabela de cursos -------------------------------------------
# criar função criar cursos ( inserir cliente C ) CRUD
def criar_curso(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Cursos (nome, duracao, preco) VALUES (?,?,?)"
        cur.execute(query,i)

#criar_curso(['Java','Duas Semanas', 70])

# Ver todos os cursos (selecionar R) CRUD
def ver_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Cursos")
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

print(ver_cursos())

# Atualizar os Cursos (Update U)
def atualizar_curso(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Cursos SET nome=?, duracao=?, preco=? WHERE id=?"
        cur.execute(query,i)

l = ['Java', 'Duas Semanas', 90, 3]
#atualizar_curso(l)


# Deletar os cursos (DELETE D)
def deletar_curso(i):
    cur = con.cursor()
    query = "DELETE FROM Cursos WHERE id=?"
    cur.execute(query,i)

deletar_curso([1])

# Tabelas de Turmas -------------------------------------------

# Criar turmas ( Inserir C)
def criar_turmas(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Turmas (nome, curso_nome, data_inicio) VALUES (?,?,?)"
        cur.execute(query,1)

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
        query = "UPDATE Turmas SET nome=?, cursos_nome=?, data_inicio=? WHERE id=?"
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
        query = "INSERT INTO Alunos (nome, email, telefone, sexo, imagem, data_nascimento, turma_nome) VALUES (?,?,?,?,?,?,?)"
        cur.execute(query,1)

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
        query = "UPDATE Alunos SET nome=?, email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, turma_nome=? WHERE id=?"
        cur.execute(query,i)

#atualizar_alunos(l)

# Deletar as Alunos (DELETE D)
def deletar_alunos(i):
    cur = con.cursor()
    query = "DELETE FROM Alunos WHERE id=?"
    cur.execute(query,i)