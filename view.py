# importando SQLite
import sqlite3 as lite

# criando conexao
try:
    con = lite.connect('Cadastro_alunos.db')
    print("Conexão com banco de dados realizado com sucesso!")
except lite.Error as e:
    print("Erro ao conectar com banco de dados:", e)

# tabela de cursos -----
# criar função criar cursos ( inserir cliente)
def criar_curso(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Cursos (nome, duracao, preco) VALUES (?,?,?)"
        cur.execute(query,i)

# criar_curso(['Python','Semanas', 50])

# Ver todos os cursos (selecionar) CRUD
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
        query = "UPDATE Cursos SET nome=?, duracao=?, preço=? EHERE id=?"
        cur.execute(query,i)
l = ["Python", "Duas Semanas", 50.0, 1]

# Deletar os cursos (DELETE D)
def deletar_curso(i):
    cur = con.cursor()
    query = "DELETE FRON Cursos WHERE id=?"
    cur.execute(query,i)


