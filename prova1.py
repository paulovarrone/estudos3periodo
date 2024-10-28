import mysql.connector
from tkinter import *
from tkinter import messagebox

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='',
    database = 'ong'
)

x = conexao.cursor()

#x.execute('create database ong')

#x.execute('create table dados(nome varchar(30), email varchar(30) primary key, telefone varchar(30), endereco varchar(30), cidade varchar(30), estado varchar(30), habilidades varchar(30))')

def inserir():
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_telefone.get()
    endereco = e_endereco.get()
    cidade = e_cidade.get()
    estado = estado_var.get()
    hab = hab_var.get()

    if any(f=='' for f in [nome,email,telefone,endereco,cidade,estado,hab]):
        messagebox.showinfo('ERRO','CAMPOS VAZIOS')
    else:
        a = 'insert into dados(nome,email,telefone,endereco,cidade,estado,habilidades) values(%s, %s, %s, %s, %s, %s, %s)'
        v = (nome,email,telefone,endereco,cidade,estado,hab)

        x.execute(a,v)
        x.execute('commit')

        for g in [e_nome,e_email,e_telefone,e_endereco,e_cidade]:
            g.delete(0,END)
        estado_var.set(NONE)
        hab_var.set(NONE)
        h_var.set(NONE)
        
        messagebox.showinfo('Sucesso','Cadastrado com sucesso')

def mostrar():
    a = "select * from dados where estado = 'Rio de Janeiro'"
    x.execute(a)
    r = x.fetchall()
    lista.delete(0,END)

    for row in r:
        lista.insert(END, '  '.join(map(str, row)))

def att():
    nome = e_nome.get()
    endereco = e_endereco.get()

    a = 'update dados set endereco = %s where nome = %s'
    v = (endereco,nome)

    x.execute(a,v)
    x.execute('commit')




i = Tk()
i.title('revisao')
i.geometry("500x500")


l_nome = Label(i, text='Nome: ')
l_nome.place(x=10, y=10)
e_nome = Entry(i)
e_nome.place(x=100, y=10)

l_email = Label(i, text='Email: ')
l_email.place(x=10, y=40)
e_email = Entry(i)
e_email.place(x=100, y=40)

l_telefone = Label(i, text='Telefone: ')
l_telefone.place(x=10, y=70)
e_telefone = Entry(i)
e_telefone.place(x=100, y=70)

l_endereco = Label(i, text='Endereço: ')
l_endereco.place(x=10, y=100)
e_endereco = Entry(i)
e_endereco.place(x=100, y=100)

l_cidade = Label(i, text='Cidade: ')
l_cidade.place(x=10, y=130)
e_cidade = Entry(i)
e_cidade.place(x=100, y=130)



estado_var = StringVar(i)
estado_var.set(None)

sp = Radiobutton(i, text='São Paulo', variable=estado_var, value='São Paulo')
sp.place(x=10, y=160)

rj = Radiobutton(i, text='Rio de Janeiro', variable=estado_var, value='Rio de Janeiro')
rj.place(x=150, y=160)



hab_var = StringVar(i)
hab_var.set(None)

h_var = StringVar(i)
h_var.set(None)

limpeza = Checkbutton(i, text='Limeza', variable=hab_var, onvalue='Limpeza')
limpeza.place(x=10, y=200)

passeio = Checkbutton(i,text='Passeio', variable=h_var, onvalue='Passeio')
passeio.place(x=100,y=200)

ali = Checkbutton(i, text='Alimentação', variable=hab_var, onvalue='Alimentação')
ali.place(x=200, y=200)

treino = Checkbutton(i, text='Treinamento', variable=hab_var, onvalue='Treinamento')
treino.place(x=320, y=200)

btn_cadastro = Button(i, text='Cadastro AJUDA', command=inserir)
btn_cadastro.place(x=100, y= 250)

btn_mostra = Button(i, text='Mostra', command=mostrar)
btn_mostra.place(x=200,y=250)

btn_att = Button(i, text='Att end', command=att)
btn_att.place(x=250,y=250)

lista = Listbox(i, width=100, height=50)
lista.place(x=10,y=300)


i.mainloop()