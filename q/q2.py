import mysql.connector
from tkinter import *
from tkinter import messagebox

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='q2'
)

x = conexao.cursor()

#x.execute('create database q2')

#x.execute('create table dados(nome varchar(30), email varchar(30) primary key, telefone varchar(30), endereco varchar(30), cidade varchar(30), estado varchar(30), limpeza varchar(30), passeio varchar(30),alimentacao varchar(30),treinamento varchar(30))')

def inserir():
    nome = enome.get()
    email = eemail.get()
    telefone = etelefone.get()
    endereco = eendereco.get()
    cidade = ecidade.get()
    estado = estado_var.get()
    limpeza = limp.get() 
    passeio =pas.get()
    alimentacao = ali.get() 
    treinamento = tre.get()
    
    if any(label=='' for label in [nome,email,telefone,endereco,cidade,estado, limpeza, passeio,alimentacao,treinamento]):
        messagebox.showinfo('ERRO','HÁ CAMPOS VAZIOS')
    else:
        a = 'insert into dados(nome, email,telefone,endereco,cidade,estado,limpeza, passeio,alimentacao,treinamento) values (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s)'
        v = (nome,email,telefone,endereco,cidade,estado,limpeza, passeio,alimentacao,treinamento)
        x.execute(a,v)
        x.execute('commit')

        for g in [enome,eemail,etelefone,eendereco,ecidade]:
            g.delete(0,END)
        for h in [estado_var,limp,pas,ali,tre]:
            h.set(None)
        messagebox.showinfo('sucesso', 'CADASTRADO COM SUCESSO')


def selecao():
    a = "select * from dados where estado = 'Rio de Janeiro' "
    x.execute(a)
    r = x.fetchall()
    lista.delete(0,END)

    for row in r:
        lista.insert(END, ' '.join(map(str,row)))
    #ou
    list(map(lambda row: lista.insert(END, ' '.join(map(str, row))), r))



def att():
    email = eemail.get()
    endereco = eendereco.get()

    if any(label=='' for label in [email,endereco]):
        messagebox.showinfo('erro','campos vazios')
    else:
        a = 'update dados set endereco = %s where email = %s'
        v = (endereco,email)
        x.execute(a,v)
        x.execute('commit')
        for i in [eendereco, eemail]:
            i.delete(0,END)
        messagebox.showinfo('SUCESSO','ENDERECO ALTERADO COM SUCESSO')


i = Tk()
i.title('Q2')
i.geometry('500x900')

lnome = Label(i,text='Nome: ')
lnome.pack()
enome = Entry(i)
enome.pack()

lemail = Label(i,text='Email: ')
lemail.pack()
eemail = Entry(i)
eemail.pack()

ltelefone = Label(i,text='Telefone')
ltelefone.pack()
etelefone = Entry(i)
etelefone.pack()

lendereco = Label(i,text='Endereco: ')
lendereco.pack()
eendereco = Entry(i)
eendereco.pack()

lcidade = Label(i,text='Cidade: ')
lcidade.pack()
ecidade = Entry(i)
ecidade.pack()

lestado = Label(i,text='ESTADO:')
lestado.pack()

estado_var = StringVar(i)
estado_var.set(None)
sp = Radiobutton(i, text='Sao Paulo', variable=estado_var, value='Sao Paulo')
sp.pack()
rj = Radiobutton(i, text='Rio de Janeiro', variable= estado_var, value='Rio de Janeiro')
rj.pack()

lhab = Label(i, text='Habilidades: ')
lhab.pack()

limp = StringVar(i)
limp.set(None)
limpeza = Checkbutton(i, text='Limpeza', variable=limp, onvalue='Limpeza')
limpeza.pack()

pas = StringVar(i)
pas.set(None)
passeio = Checkbutton(i, text='Passeio', variable=pas, onvalue='Passeio')
passeio.pack()

ali = StringVar(i)
ali.set(None)
alimentacao = Checkbutton(i,text='Alimentaçao', variable=ali, onvalue='Alimentaçao')
alimentacao.pack()

tre = StringVar(i)
tre.set(None)
treino = Checkbutton(i,text='Treinamento', variable=tre, onvalue='Treinamento')
treino.pack()

cadastro = Button(i, text='Cadastro', command=inserir)
cadastro.pack()

alterar = Button(i,text='Alterar', command=att)
alterar.pack()

selecionar = Button(i,text='Selecionar', command=selecao)
selecionar.pack()

lista = Listbox(i, width=50, height=100)
lista.pack()








i.mainloop()
