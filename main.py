from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# importando pillow
from PIL import ImageTk, Image

#tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# definir cores
# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co5 = "#003452"   # azul
co6 = "#ef5350"   # vermelha

co7 = "#038cfc"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

# Crando Janela
janela = Tk()
janela.title("")
janela.geometry("850x620")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Criando Frames
frame_logo = Frame(janela, width=850, height=52, bg=co5)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)

# Trabalhando no frame logo -------------------------------------------

app_lg = Image.open('kimono.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Allianz Jiu Jitsu Itaquera", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('ivy 15 bold'), bg=co5, fg=co1)
app_logo.place(x=0, y=0)

# função para cadastrar alunos
def alunos():
    #Criar campo de entrada nome
    l_nome = Label(frame_detalhes, text="Nome *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=4, y=10)
    e_nome = Entry(frame_detalhes, width=45, justify='left', relief='solid')
    e_nome.place(x=7, y=40)

    #Criar campo de entrada email
    l_email = Label(frame_detalhes, text="e-mail *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_email.place(x=4, y=70)
    e_email = Entry(frame_detalhes, width=45, justify='left', relief='solid')
    e_email.place(x=7, y=100)

    #Criar campo de entrada telefone
    l_telefone = Label(frame_detalhes, text="Telefone *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_telefone.place(x=4, y=130)
    e_telefone = Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_telefone.place(x=7, y=160)

    # seleção de genero
    l_genero = Label(frame_detalhes, text="Sexo *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_genero.place(x=190, y=130)
    c_genero = ttk.Combobox(frame_detalhes, width=12, font=('Ivy 8 bold'))
    c_genero["values"] = ("Masculino", "Feminino")
    c_genero.place(x=190, y=160)

    # Selecionar data de nascimento
    l_data_nascimento = Label(frame_detalhes, text="Data de nascimento *", height=1, anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    l_data_nascimento.place(x=446, y=10)
    data_nascimento = DateEntry(frame_detalhes, width=18, background="darkblue", foreground="white", borderwidth=2, year=2023 )
    data_nascimento.place(x=450, y=40)

    # campo CPF
    l_cpf = Label(frame_detalhes, text="CPF *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_cpf.place(x=446, y=70)
    e_cpf = Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_cpf.place(x=450, y=100)

    # buscando as turmas
    turmas = ["Iniciante", "Graduados", "Kids", "May Thay", "Ioga", "Outros"]
    turma = []

    for i in turmas:
        turma.append(i)

    l_turma = Label(frame_detalhes, text="Turma *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_turma.place(x=446, y=130)
    c_turma = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
    c_turma["values"] = (turma)
    c_turma.place(x=450, y=160)


    # Função para selecionar imagem

    global imagem, imagem_string, l_imagem

    def escolher_imagem():
        global imagem, imagem_string, l_imagem

        imagem = Image.open('allianz.png')
        imagem = imagem.resize((130,130))
        imagem = ImageTk.PhotoImage(imagem)
        l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
        l_imagem.place(x=300, y=10)

    button_carregar = Button(frame_detalhes, command=escolher_imagem,  text="Carregar foto".upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE , font=('ivy 7 bold'), bg=co1, fg=co0)
    button_carregar.place(x=300, y=160)
       

# função para adicionar modalidades e turmas
def adicionar():
    # Criando frames para tabelas -----
    frame_tabela_modalidade = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_modalidade.grid(row=0, column=0, pady=0, padx=10, sticky=NSEW)

    frame_tabela_linha = Frame(frame_tabela, width=30, height=200, bg=co1)
    frame_tabela_linha.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)

    frame_tabela_turma = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_turma.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)

    l_nome = Label(frame_detalhes, text="Nome da modalidade", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=4, y=10)
    e_nome_modalidade = Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_nome_modalidade.place(x=7, y=40)

    l_duracao = Label(frame_detalhes, text="Duração *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_duracao.place(x=4, y=70)
    e_duracao = Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_duracao.place(x=7, y=100)

    l_mensalidade = Label(frame_detalhes, text="Mensalidade *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_mensalidade.place(x=4, y=130)
    e_mensalidade = Entry(frame_detalhes, width=10, justify='left', relief='solid')
    e_mensalidade.place(x=7, y=160)

    # criar botão carregar
    button_carregar = Button(frame_detalhes, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1 )
    button_carregar.place(x=107, y=160)

    # criar botão atualizar
    button_atualizar = Button(frame_detalhes, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1 )
    button_atualizar.place(x=187, y=160)

    # criar botão deletar
    button_deletar = Button(frame_detalhes, anchor=CENTER, text='Delete'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1 )
    button_deletar.place(x=267, y=160)

    # Tabela modalidade
    def mostrar_modalidades():
        app_nome = Label(frame_tabela_modalidade, text="Tabela de Modalidades", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        #creating a treeview with dual scrollbars
        list_header = ['ID','modalidade','Duração','Preço']

        df_list = []

        global tree_modalidade

        tree_modalidade = ttk.Treeview(frame_tabela_modalidade, selectmode="extended",columns=list_header, show="headings")

        #vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela_modalidade, orient="vertical", command=tree_modalidade.yview)
        #horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela_modalidade, orient="horizontal", command=tree_modalidade.xview)

        tree_modalidade.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_modalidade.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_modalidade.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","e","e"]
        h=[30,150,80,60]
        n=0

        for col in list_header:
            tree_modalidade.heading(col, text=col.title(), anchor=NW)
            #adjust the column's width to the header string
            tree_modalidade.column(col, width=h[n],anchor=hd[n])

            n+=1

        for item in df_list:
            tree_modalidade.insert('', 'end', values=item)

    mostrar_modalidades()

    # linha separatória ---------------------------
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    l_linha.place(x=374, y=10)
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    l_linha.place(x=372, y=10)

    # linha separatória tabela
    l_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=130, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    l_linha.place(x=6, y=10)
    l_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=130, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    l_linha.place(x=4, y=10)


    # detalhes da Turma ---------------------------
    l_nome = Label(frame_detalhes, text="Nome da Turma *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=404, y=10)
    e_nome_turma = Entry(frame_detalhes, width=35, justify='left', relief="solid")
    e_nome_turma.place(x=407, y=40)

    l_turma = Label(frame_detalhes, text="modalidade *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_turma.place(x=404, y=70)

    # buscando os modalidades
    modalidades = ["Graduado", "Iniciante", "Kids", "Muy Thay", "Ioga"]
    modalidade = []

    for i in modalidades:
        modalidade.append(i)

    c_modalidade = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
    c_modalidade["values"] = (modalidade)
    c_modalidade.place(x=407, y=100)

    l_data_inicio = Label(frame_detalhes, text="Data de inicio *", height=1, anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    l_data_inicio.place(x=400, y=130)
    data_inicio = DateEntry(frame_detalhes, width=10, background="darkblue", foreground="white", borderwidth=2, year=2023 )
    data_inicio.place(x=407, y=160)

    # criar botão carregar
    button_carregar = Button(frame_detalhes, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1 )
    button_carregar.place(x=507, y=160)

    # criar botão atualizar
    button_atualizar = Button(frame_detalhes, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1 )
    button_atualizar.place(x=587, y=160)

    # criar botão deletar
    button_deletar = Button(frame_detalhes, anchor=CENTER, text='Delete'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1 )
    button_deletar.place(x=667, y=160)

    # Tabela Turmas
    def mostrar_turma():
        app_nome = Label(frame_tabela_turma, text="Tabela de Turma", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        #creating a treeview with dual scrollbars
        list_header = ['ID','Nome da Turma','modalidade','Inicio']

        df_list = []

        global tree_turma

        tree_turma = ttk.Treeview(frame_tabela_turma, selectmode="extended",columns=list_header, show="headings")

        #vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela_turma, orient="vertical", command=tree_turma.yview)
        #horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela_turma, orient="horizontal", command=tree_turma.xview)

        tree_turma.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_turma.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_turma.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","e","e"]
        h=[30,130,150,80]
        n=0

        for col in list_header:
            tree_turma.heading(col, text=col.title(), anchor=NW)
            #adjust the column's width to the header string
            tree_turma.column(col, width=h[n],anchor=hd[n])

            n+=1

        for item in df_list:
            tree_turma.insert('', 'end', values=item)

    mostrar_turma()

# função para salvar 
def salvar():
    print('Salvar')


# função de controle -----------------------------------------------------

def control(i):
    # cadastro de aluno
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        # chamando a função aluno
        alunos()

    if i == 'adicionar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        # chamando a função adicionar
        adicionar()

    if i == 'salvar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        # chamando a função salvar
        salvar()

# Criando os botoes------------------------------------------------

app_img_cadastro = Image.open('add.png')
app_img_cadastro = app_img_cadastro.resize((18,18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, command=lambda:control('cadastro'), image=app_img_cadastro, text="Cadastro", width=100, compound=LEFT, overrelief=RIDGE , font=('ivy 11 bold'), bg=co1, fg=co0)
app_cadastro.place(x=10, y=30)


app_img_adicionar = Image.open('add.png')
app_img_adicionar = app_img_adicionar.resize((18,18))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_dados, command=lambda:control('adicionar'), image=app_img_adicionar, text="Adicionar", width=100, compound=LEFT, overrelief=RIDGE , font=('ivy 11 bold'), bg=co1, fg=co0)
app_adicionar.place(x=123, y=30)


app_img_salvar = Image.open('salvar.png')
app_img_salvar = app_img_salvar.resize((18,18))
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
app_salvar = Button(frame_dados, command=lambda:control('salvar'), image=app_img_salvar, text="Salvar", width=100, compound=LEFT, overrelief=RIDGE , font=('ivy 11 bold'), bg=co1, fg=co0)
app_salvar.place(x=236, y=30)


alunos()
janela.mainloop()