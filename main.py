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

# importar View
from view import *

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
janela.geometry("1020x620")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Criando Frames
frame_logo = Frame(janela, width=1020, height=52, bg=co5)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=1020, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=1020, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=1020, height=200, bg=co1)
frame_tabela.grid(row=31, column=0, pady=0, padx=10, sticky=NSEW)

# Trabalhando no frame logo -------------------------------------------

app_lg = Image.open('kimono.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Academy Jiu Jitsu ", width=1020, compound=LEFT, relief=RAISED, anchor=NW, font=('ivy 15 bold'), bg=co5, fg=co1)
app_logo.place(x=0, y=0)


# função para cadastrar alunos
def alunos():

    # função novo aluno
    def novo_aluno():
        # variaveis para buscar a foto do aluno
        global imagem, imagem_string, l_imagem

        nome = e_nome.get()
        email = e_email.get()
        sexo = c_genero.get()
        data_nascimento = c_data_nascimento.get()
        imagem = imagem_string
        turma_nome = c_turma.get()
        faixa = e_faixa.get()
        grau = c_grau.get()
        telefone = e_telefone.get()
        cpf = e_cpf.get()
        

        lista = [nome, email, sexo, data_nascimento, imagem, turma_nome, faixa, grau, telefone, cpf]

        # verificar se algum campo esteja vazio
        for i in lista:
            if i=="":
                messagebox.showerror("Erro", "Preencher todos os campos")
                return
        
        # inserindo os dados no Banco de Dados
        criar_alunos(lista)

        # Mostrando a mensagem de sucesso
        messagebox.showinfo("Sucesso", "OS dados foram inseridos com sucesso")

        # Limpando os campos de entrada
        e_nome.delete(0, END)
        e_email.delete(0, END)
        c_genero.delete(0, END)
        c_data_nascimento.delete(0, END)
        c_turma.delete(0, END)
        e_faixa.delete(0, END)
        c_grau.delete(0, END)
        e_telefone.delete(0, END)
        e_cpf.delete(0, END)
        # Mostrando os valores na tabela
        ver_alunos()

    # criada a função atualizar aluno 
    def update_aluno():
        global imagem, imagem_string, l_imagem

        try:
            tree_itens = tree_aluno.focus()
            tree_dicionario = tree_aluno.item(tree_itens)
            tree_lista = tree_dicionario["values"]

            valor_id = tree_lista[0]

            # Limpando os campos de entrada
            e_nome.delete(0, END)
            e_email.delete(0, END)
            c_genero.delete(0, END)
            c_data_nascimento.delete(0, END)
            c_turma.delete(0, END)
            e_faixa.delete(0, END)
            c_grau.delete(0, END)
            e_telefone.delete(0, END)
            e_cpf.delete(0, END)

            # Inserindo os valores nos campos de
            e_nome.insert(0, tree_lista[1])
            e_email.insert(0, tree_lista[2])
            c_genero.insert(0, tree_lista[3])
            c_data_nascimento.insert(0, tree_lista[4])
            c_turma.insert(0, tree_lista[6])
            e_faixa.insert(0, tree_lista[7])
            c_grau.insert(0, tree_lista[8])
            e_telefone.insert(0, tree_lista[9])
            e_cpf.insert(0, tree_lista[10])
        
            
            imagem = tree_lista[5]
            imagem_string = imagem 

            # abrindo a imagem
            imagem = Image.open(imagem)
            imagem = imagem.resize((130,130))
            imagem = ImageTk.PhotoImage(imagem)
            l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
            l_imagem.place(x=300, y=10)
            # Função atualizar 
            
            def update():
                
                nome = e_nome.get()
                email = e_email.get()
                sexo = c_genero.get()
                data_nascimento = c_data_nascimento.get()
                imagem = imagem_string
                turma_nome = c_turma.get()
                faixa = e_faixa.get()
                grau = c_grau.get()
                telefone = e_telefone.get()
                cpf = e_cpf.get()

                lista = [nome, email, sexo, data_nascimento, imagem, turma_nome, faixa, grau, telefone, cpf, valor_id]

                # codigo para verificar se está vazio algum campo
                for i in lista:
                    if i== "":
                        messagebox.showerror("Erro", "Preencher todos os campos")
                        return
                
                # Atualizando os dados 
                atualizar_alunos(lista)

                # mostrar mensagem de sucesso
                messagebox.showinfo("Sucesso", "Os dados foram atualizados com sucesso")

                e_nome.insert(0, END)
                e_email.insert(0, END)
                c_genero.insert(0, END)
                c_data_nascimento.insert(0, END)
                c_turma.insert(0, END)
                e_faixa.insert(0, END)
                c_grau.insert(0, END)
                e_telefone.insert(0, END)
                e_cpf.insert(0, END)

                # mostrar tabela das modalidades após inserir os dados
                ver_alunos()

                # Limpando os campos de entrada
                e_nome.delete(0, END)
                e_email.delete(0, END)
                c_genero.delete(0, END)
                c_data_nascimento.delete(0, END)
                c_turma.delete(0, END)
                e_faixa.delete(0, END)
                c_grau.delete(0, END)
                e_telefone.delete(0, END)
                e_cpf.delete(0, END)

                # apagando o botão salvar após salvar os dados
                button_update.destroy()  
            
            button_update = Button(frame_detalhes, command=update, anchor=CENTER, text='Salvar atualização'.upper(), overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1 )
            button_update.place(x=827, y=130)

        except IndexError:
            messagebox.showerror("Erro", "Selecione uma dos Alunos na tabela")

    # Função deletar modalidade
    def delete_aluno():
        try:
            tree_itens = tree_aluno.focus()
            tree_dicionario = tree_aluno.item(tree_itens)
            tree_lista = tree_dicionario["values"]

            valor_id = tree_lista[0]

            # apagar os dados no banco de dados
            deletar_alunos([valor_id])

            # mostrar mensagem de sucesso
            messagebox.showinfo("Sucesso", "Os dados foram deletados com sucesso")

            # mostrar tabela das modalidades após inserir os dados
            ver_alunos()

        except IndexError:
            messagebox.showerror("Erro", "Selecione um dos Alunos da tabela")


    #Criar campo de entrada nome
    l_nome = Label(frame_detalhes, text="Nome *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=4, y=10)
    e_nome = Entry(frame_detalhes, width=45, justify='left', relief='solid')
    e_nome.place(x=7, y=40)

     #Criar campo de entrada email
    l_email = Label(frame_detalhes, text="e-mail *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_email.place(x=4, y=60)
    e_email = Entry(frame_detalhes, width=45, justify='left', relief='solid')
    e_email.place(x=7, y=80)

    # #Criar campo de entrada faixa
    l_faixa = Label(frame_detalhes, text="Faixa*", height=1, anchor=NW, font=('Ivy 7'), bg=co1, fg=co4)
    l_faixa.place(x=4, y=115)
    e_faixa = Entry(frame_detalhes, width=15, justify='left', relief='solid')
    e_faixa.place(x=7, y=130)

    # seleção de grau
    l_grau = Label(frame_detalhes, text="Grau *", height=1, anchor=NW, font=('Ivy 7'), bg=co1, fg=co4)
    l_grau.place(x=190, y=115)
    c_grau = ttk.Combobox(frame_detalhes, width=12, font=('Ivy 8 bold'))
    c_grau["values"] = ("0", "1", "2", "3", "4")
    c_grau.place(x=190, y=130)

    #Criar campo de entrada telefone
    l_telefone = Label(frame_detalhes, text="Telefone *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_telefone.place(x=4, y=150)
    e_telefone = Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_telefone.place(x=7, y=170)

    # seleção de genero
    l_genero = Label(frame_detalhes, text="Sexo *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_genero.place(x=190, y=150)
    c_genero = ttk.Combobox(frame_detalhes, width=12, font=('Ivy 8 bold'))
    c_genero["values"] = ("Masc", "Fem")
    c_genero.place(x=190, y=170)

    # Selecionar data de nascimento
    l_data_nascimento = Label(frame_detalhes, text="Data de nascimento *", height=1, anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    l_data_nascimento.place(x=446, y=10)
    c_data_nascimento = DateEntry(frame_detalhes, width=18, background="darkblue", foreground="white", borderwidth=2, year=2023 )
    c_data_nascimento.place(x=450, y=40)

    # campo CPF
    l_cpf = Label(frame_detalhes, text="CPF *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_cpf.place(x=446, y=70)
    e_cpf = Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_cpf.place(x=450, y=100)

    # buscando as turmas
    turmas = ver_turmas()
    turma = []

    for i in turmas:
        turma.append(i[1])

    l_turma = Label(frame_detalhes, text="Turma *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_turma.place(x=446, y=130)
    c_turma = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
    c_turma["values"] = (turma)
    c_turma.place(x=450, y=160)


    # Função para selecionar imagem

    global imagem, imagem_string, l_imagem
    imagem = None
    imagem_string = None
    l_imagem = None

    def escolher_imagem():
        global imagem, imagem_string, l_imagem
        # selecionar foto dos arquivos 
        imagem = fd.askopenfilename()
        imagem_string = imagem

        # abrindo imagem
        imagem = Image.open(imagem)
        imagem = imagem.resize((130,130))
        imagem = ImageTk.PhotoImage(imagem)

        if l_imagem:
            l_imagem.config(image=imagem)
        else:
            l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
            l_imagem.place(x=300, y=10)
        
        l_imagem.imge = imagem # Manter referência à imagem para evitar garbage collection

        button_carregar["text"] = "Trocar de Foto"

    button_carregar = Button(frame_detalhes, command=escolher_imagem,  text="Carregar foto".upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE , font=('ivy 7 bold'), bg=co1, fg=co0)
    button_carregar.place(x=300, y=160)

    # linha separatória ---------------------------
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    l_linha.place(x=610, y=10)
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    l_linha.place(x=608, y=10)

        
        # Função procurar aluno 
    def procurar_aluno():
        global imagem, imagem_string, l_imagem

        try:
            # Obtém o valor do campo de entrada (ID ou nome do aluno)
            nome = e_localizar_nome.get()
            # email = e_email.get()
            # sexo = c_genero.get()
            # data_nascimento = c_data_nascimento.get()
            # imagem = imagem_string
            # turma_nome = c_turma.get()
            # faixa = e_faixa.get()
            # grau = c_grau.get()
            # telefone = e_telefone.get()
            # cpf = e_cpf.get()


            # Verifica se o valor de busca não está vazio
            if not nome:
                messagebox.showerror("Erro", "Por favor, insira um nome para buscar")
                return

            # Limpa a seleção anterior na treeview
            for item in tree_aluno.selection():
                tree_aluno.selection_remove(item)

            # Itera sobre todos os itens na treeview para procurar o aluno
            encontrado = False
            for item in tree_aluno.get_children():
                tree_dicionario = tree_aluno.item(item)
                tree_lista = tree_dicionario["values"]

                # valor_id = tree_lista[0]
                # Supondo que o ID do aluno está na primeira posição e o nome na segunda
                valor_id = tree_lista[0]
                e_aluno = tree_lista[1]


            # Verifica se o valor buscado corresponde ao ID ou nome do aluno
                if nome == valor_id or nome.lower() in e_aluno.lower():
                    tree_aluno.selection_add(item)
                    tree_aluno.see(item)  # Rolagem automática para o item encontrado
                    messagebox.showinfo("Sucesso", f"Aluno encontrado: {e_aluno}")
                    encontrado = True
                    break

            
                # Se não encontrar nenhum aluno correspondente
            if not encontrado:
                messagebox.showinfo("Informação", "Aluno não encontrado")    

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    # Criar campo de busca 
    l_localizar_nome = Label(frame_detalhes, text="Procurar Aluno [ Entra com nome ] ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_localizar_nome.place(x=627, y=10)
    e_localizar_nome = Entry(frame_detalhes, width=17, justify='center', relief='solid', font=("Ivy 10"))
    e_localizar_nome.place(x=630, y=35)

    botao_procurar = Button(frame_detalhes, command=procurar_aluno, anchor=CENTER, text="Procurar", width=9, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co1, fg=co4)
    botao_procurar.place(x=757, y=35)

    # criar botão salvar
    button_salvar = Button(frame_detalhes, command=novo_aluno, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1 )
    button_salvar.place(x=627, y=110)

    # criar botão atualizar
    button_atualizar = Button(frame_detalhes, command=update_aluno, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1 )
    button_atualizar.place(x=627, y=135)

    # criar botão deletar
    button_deletar = Button(frame_detalhes, command=delete_aluno, anchor=CENTER, text='Delete'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1 )
    button_deletar.place(x=627, y=160)


    def carregar_dados_aluno():
        global imagem, imagem_string, l_imagem

        try:

            
            tree_itens = tree_aluno.focus()
            tree_dicionario = tree_aluno.item(tree_itens)
            tree_lista = tree_dicionario["values"]
            

            valor_id = tree_lista[0]

            # Limpando os campos de entrada
            e_nome.delete(0, END)
            e_email.delete(0, END)
            c_genero.delete(0, END)
            c_data_nascimento.delete(0, END)
            c_turma.delete(0, END)
            e_faixa.delete(0, END)
            c_grau.delete(0, END)
            e_telefone.delete(0, END)
            e_cpf.delete(0, END)

            # Inserindo os valores nos campos de
            e_nome.insert(0, tree_lista[1])
            e_email.insert(0, tree_lista[2])
            c_genero.insert(0, tree_lista[3])
            c_data_nascimento.insert(0, tree_lista[4])
            c_turma.insert(0, tree_lista[6])
            e_faixa.insert(0, tree_lista[7])
            c_grau.insert(0, tree_lista[8])
            e_telefone.insert(0, tree_lista[9])
            e_cpf.insert(0, tree_lista[10])

            imagem = tree_lista[5]
            imagem_string = imagem

            # abrindo a imagem
            imagem = Image.open(imagem)
            imagem = imagem.resize((130,130))
            imagem = ImageTk.PhotoImage(imagem)
            l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
            l_imagem.place(x=300, y=10)


            def ver_update():
                
                nome = e_nome.get()
                email = e_email.get()
                sexo = c_genero.get()
                data_nascimento = c_data_nascimento.get()
                imagem = imagem_string
                turma_nome = c_turma.get()
                faixa = e_faixa.get()
                grau = c_grau.get()
                telefone = e_telefone.get()
                cpf = e_cpf.get()

                lista = [nome, email, sexo, data_nascimento, imagem, turma_nome, faixa, grau, telefone, cpf, valor_id]

                # codigo para verificar se está vazio algum campo
                for i in lista:
                    if i== "":
                        messagebox.showerror("Erro", "Preencher todos os campos")
                        return
                
                # Atualizando os dados 
                atualizar_alunos(lista)

                # mostrar mensagem de sucesso
                messagebox.showinfo("Sucesso", "Os dados foram carregados com sucesso")

                e_nome.insert(0, END)
                e_email.insert(0, END)
                c_genero.insert(0, END)
                c_data_nascimento.insert(0, END)
                c_turma.insert(0, END)
                e_faixa.insert(0, END)
                c_grau.insert(0, END)
                e_telefone.insert(0, END)
                e_cpf.insert(0, END)

                # mostrar tabela das modalidades após inserir os dados
                ver_alunos()

                # Limpando os campos de entrada
                e_nome.delete(0, END)
                e_email.delete(0, END)
                c_genero.delete(0, END)
                c_data_nascimento.delete(0, END)
                c_turma.delete(0, END)
                e_faixa.delete(0, END)
                c_grau.delete(0, END)
                e_telefone.delete(0, END)
                e_cpf.delete(0, END)

            

            l_imagem.image = imagem # Manter a referencia à imagem para evitar garbage collection


        except IndexError:
            messagebox.showerror("Erro", "Selecione um aluno na tabela")
        
    # criar botão ver
    button_ver = Button(frame_detalhes, command=carregar_dados_aluno, anchor=CENTER, text='Ver'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co5, fg=co1 )
    button_ver.place(x=727, y=160)


    #Tabela Aluno
    def mostrar_alunos():
        app_nome = Label(frame_tabela, text="Tabela de Alunos", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # creating a treeview with dual scrollbars
        list_header = ['id','Nome','email', 'sexo', 'Data', 'imagem', 'Modalidade', 'faixa', 'grau', 'Telefone', 'CPF']
                    
        df_list = ver_alunos()

        global tree_aluno

        tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
        # horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)

        tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_aluno.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","nw","center","center","center","center","center","center","center","center"]
        h=[40,150,150,70,70,70,70,70,80,80,100]
        n=0

        for col in list_header:
            tree_aluno.heading(col, text=col.title(), anchor=NW)
            #adjust the column's width to the header string
            tree_aluno.column(col, width=h[n],anchor=hd[n])

            n+=1

        for item in df_list:
            tree_aluno.insert('', 'end', values=item)

    mostrar_alunos()



# função para adicionar modalidades e turmas
def adicionar():
    # Criando frames para tabelas -----
    frame_tabela_modalidade = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_modalidade.grid(row=0, column=0, pady=0, padx=10, sticky=NSEW)

    frame_tabela_linha = Frame(frame_tabela, width=30, height=200, bg=co1)
    frame_tabela_linha.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)

    frame_tabela_turma = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_turma.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)

    # Detalhes da Modalidade -------------------------------------------------------

    # função para adicionar nova modalidade ---
    def nova_modalidade():
        nome = e_nome_modalidade.get()
        periodo = e_periodo.get()
        mensalidade = e_mensalidade.get()

        lista = [nome, periodo, mensalidade]
        # codigo para verificar se está vazio algum campo
        for i in lista:
            if i== "":
                messagebox.showerror("Erro", "Preencher todos os campos")
                return
        
        # Inserir os dados 
        criar_modalidade(lista)

        # mostrar mensagem de sucesso
        messagebox.showinfo("Sucesso", "Os dados foram inseridos com sucesso")

        e_nome_modalidade.delete(0, END)
        e_periodo.delete(0, END)
        e_mensalidade.delete(0, END)

        # mostrar tabela das modalidades após inserir os dados
        ver_modalidades()
    # adcionar função para apagar os campos antes de inserir os novos dados
    # função para adicionar nova modalidade ---
    # Precisa inserir um comando para identificar se os dados correspondem aos mesmos já no banco de dados
    def update_modalidade():
        try:
            tree_itens = tree_modalidade.focus()
            tree_dicionario = tree_modalidade.item(tree_itens)
            tree_lista = tree_dicionario["values"]

            valor_id = tree_lista[0]
            # inserir função para apagar os campos antes de inserir novos dados
            # inserindo os valores nas entries
            e_nome_modalidade.insert(0, tree_lista[1])
            e_periodo.insert(0, tree_lista[2])
            e_mensalidade.insert(0, tree_lista[3])

            # Função atualizar 
            def update():
                
                nome = e_nome_modalidade.get()
                periodo = e_periodo.get()
                mensalidade = e_mensalidade.get()

                lista = [nome, periodo, mensalidade, valor_id]

                # codigo para verificar se está vazio algum campo
                for i in lista:
                    if i== "":
                        messagebox.showerror("Erro", "Preencher todos os campos")
                        return
                
                # Inserir os dados 
                atualizar_modalidade(lista)

                # mostrar mensagem de sucesso
                messagebox.showinfo("Sucesso", "Os dados foram inseridos com sucesso")

                e_nome_modalidade.delete(0, END)
                e_periodo.delete(0, END)
                e_mensalidade.delete(0, END)

                # mostrar tabela das modalidades após inserir os dados
                ver_modalidades()

                # apagando o botão salvar após salvar os dados
                button_salvar.destroy()  
            
            button_salvar = Button(frame_detalhes, command=update, anchor=CENTER, text='Salvar atualização'.upper(), overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1 )
            button_salvar.place(x=227, y=130)

        except IndexError:
            messagebox.showerror("Erro", "Selecione uma das categorias na tabela")


    # Função deletar modalidade
    def delete_modalidade():
        try:
            tree_itens = tree_modalidade.focus()
            tree_dicionario = tree_modalidade.item(tree_itens)
            tree_lista = tree_dicionario["values"]

            valor_id = tree_lista[0]

            # apagar os dados no banco de dados
            deletar_modalidade([valor_id])

            # mostrar mensagem de sucesso
            messagebox.showinfo("Sucesso", "Os dados foram deletados com sucesso")

            # mostrar tabela das modalidades após inserir os dados
            ver_modalidades()

        except IndexError:
            messagebox.showerror("Erro", "Selecione uma das modalidades da tabela")



    l_nome = Label(frame_detalhes, text="Nome da modalidade", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=4, y=10)
    e_nome_modalidade = Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_nome_modalidade.place(x=7, y=40)

    l_periodo = Label(frame_detalhes, text="Período *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_periodo.place(x=4, y=70)
    e_periodo = Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_periodo.place(x=7, y=100)

    l_mensalidade = Label(frame_detalhes, text="Mensalidade *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_mensalidade.place(x=4, y=130)
    e_mensalidade = Entry(frame_detalhes, width=10, justify='left', relief='solid')
    e_mensalidade.place(x=7, y=160)

    # criar botão carregar
    button_carregar = Button(frame_detalhes, command=nova_modalidade, anchor=CENTER, text='Criar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1 )
    button_carregar.place(x=107, y=160)

    # criar botão atualizar
    button_atualizar = Button(frame_detalhes, command=update_modalidade ,anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1 )
    button_atualizar.place(x=187, y=160)

    # criar botão deletar
    button_deletar = Button(frame_detalhes, command= delete_modalidade, anchor=CENTER, text='Delete'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1 )
    button_deletar.place(x=267, y=160)

    # Tabela modalidade
    # adcionada a tabela com dados do aluno
    def mostrar_modalidades():
        app_nome = Label(frame_tabela_modalidade, text="Tabela de Modalidades", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        #creating a treeview with dual scrollbars
        list_header = ['ID','modalidade','Periodo','Mensalidade']

        df_list = ver_modalidades()

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
    # função nova turma

    def nova_turma():
        nome = e_nome_turma.get()
        curso = c_modalidade.get()
        data = data_inicio.get()

        lista = [nome, curso, data]
        # codigo para verificar se está vazio algum campo
        for i in lista:
            if i== "":
                messagebox.showerror("Erro", "Preencher todos os campos")
                return
        
        # Inserir os dados 
        criar_turma(lista)

        # mostrar mensagem de sucesso
        messagebox.showinfo("Sucesso", "Os dados foram inseridos com sucesso")

        e_nome_turma.delete(0, END)
        c_modalidade.delete(0, END)
        data_inicio.delete(0, END)

        # mostrar tabela das turmas após inserir os dados
        ver_modalidades()

        # função atualizar turma
    def update_turma():
        try:
            tree_itens = tree_turma.focus()
            tree_dicionario = tree_turma.item(tree_itens)
            tree_lista = tree_dicionario["values"]

            valor_id = tree_lista[0]
            # inserir função para apagar os campos antes de inserir novos dados
            # inserindo os valores nas entries
            e_nome_turma.insert(0, tree_lista[1])
            c_modalidade.insert(0, tree_lista[2])
            data_inicio.insert(0, tree_lista[3])

            # Função atualizar 
            def update():
                    
                nome = e_nome_turma.get()
                curso = c_modalidade.get()
                data = data_inicio.get()

                lista = [nome, curso, data, valor_id]

                # codigo para verificar se está vazio algum campo
                for i in lista:
                    if i== "":
                        messagebox.showerror("Erro", "Preencher todos os campos")
                        return
                    
                # Inserir os dados 
                atualizar_turmas(lista)

                # mostrar mensagem de sucesso
                messagebox.showinfo("Sucesso", "Os dados foram inseridos com sucesso")

                e_nome_turma.delete(0, END)
                c_modalidade.delete(0, END)
                data_inicio.delete(0, END)

                    # mostrar tabela das modalidades após inserir os dados
                ver_turmas()

                # apagando o botão salvar após salvar os dados
                button_salvar.destroy()  
           #     
            button_salvar = Button(frame_detalhes, command=update, anchor=CENTER, text='Salvar atualização'.upper(), overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1 )
            button_salvar.place(x=404, y=130)

        except IndexError:
            messagebox.showerror("Erro", "Selecione uma das categorias na tabela")

    # Função deletar turma
    def delete_turma():
        try:
            tree_itens = tree_turma.focus()
            tree_dicionario = tree_turma.item(tree_itens)
            tree_lista = tree_dicionario["values"]

            valor_id = tree_lista[0]

            # apagar os dados no banco de dados
            deletar_turma([valor_id])

            # mostrar mensagem de sucesso
            messagebox.showinfo("Sucesso", "Os dados foram deletados com sucesso")

            # mostrar tabela das turmas após inserir os dados
            ver_turmas()

        except IndexError:
            messagebox.showerror("Erro", "Selecione uma das modalidades da tabela")

    l_nome = Label(frame_detalhes, text="Nome da Turma *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=404, y=10)
    e_nome_turma = Entry(frame_detalhes, width=35, justify='left', relief="solid")
    e_nome_turma.place(x=407, y=40)

    l_turma = Label(frame_detalhes, text="Turma *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_turma.place(x=407, y=70)

    # buscando os modalidades
    modalidades = ver_modalidades()
    modalidade = []

    for i in modalidades:
        modalidade.append(i[1])

    c_modalidade = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
    c_modalidade["values"] = (modalidade)
    c_modalidade.place(x=407, y=100)

    l_data_inicio = Label(frame_detalhes, text="Data de inicio *", height=1, anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    l_data_inicio.place(x=404, y=130)
    data_inicio = DateEntry(frame_detalhes, width=10, background="darkblue", foreground="white", borderwidth=2, year=2023 )
    data_inicio.place(x=407, y=160)

    # criar botão carregar
    button_carregar = Button(frame_detalhes, command=nova_turma, anchor=CENTER, text='Criar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1 )
    button_carregar.place(x=507, y=160)

    # criar botão atualizar
    button_atualizar = Button(frame_detalhes, command=update_turma, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1 )
    button_atualizar.place(x=587, y=160)

    # criar botão deletar
    button_deletar = Button(frame_detalhes, command=delete_turma, anchor=CENTER, text='Delete'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1 )
    button_deletar.place(x=667, y=160)

    # Tabela Turmas
    def mostrar_turma():
        app_nome = Label(frame_tabela_turma, text="Tabela de Turma", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        #creating a treeview with dual scrollbars
        list_header = ['ID','Nome da Turma','Curso','Inicio']

        df_list = ver_turmas()

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
# incluir nessa função a funcionalidade de gerar arquivo excel, pdf 

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