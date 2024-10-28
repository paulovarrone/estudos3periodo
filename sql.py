import mysql.connector
from tkinter import *
from tkinter import messagebox

conexao = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'prova'
)

x = conexao.cursor()

#x.execute('create database prova')
#x.execute('create table aluno(id int primary key auto_increment, nome varchar(30), disciplina varchar(30), nota float)')

def cad():
    nome = e_nome.get()
    disciplina = e_disciplina.get()
    nota = e_nota.get()

    if nome == '' or disciplina == '' or nota == '':
        messagebox.showinfo('erro', 'CAMPOS VAZIOS')
    else:
        a = 'insert into aluno(nome,disciplina,nota) values(%s,%s,%s)'
        v =(nome,disciplina,nota)
        x.execute(a,v)
        x.execute('commit')

        e_nome.delete(0,END)
        e_disciplina.delete(0,END)
        e_nota.delete(0,END)
        messagebox.showinfo('SIM', 'INSERIDO COM SUCESSO')

def mostrar(): 
    a = 'select * from aluno where nota > 7.0'
    x.execute(a)
    r = x.fetchall()

    listbox.delete(0, END)

    for row in r:
        listbox.insert(END, f'{row[0]} Nome: {row[1]} - Disciplina: {row[2]} - Nota: {row[3]}')

def updt():
    nome = e_nome.get()

    if nome == '':
        messagebox.showinfo('erro', 'CAMPOS nome VAZIO')
    else:
        a = 'update aluno set nota = NULL where nome = %s'
        v = (nome,)
        x.execute(a,v)
        x.execute('commit')

def deletar():
    nome = e_nome.get()

    if nome == '':
        messagebox.showinfo('erro', 'CAMPOS nome VAZIO')
    else:
        a = 'delete from aluno where nome = %s'
        v = (nome,)
        x.execute(a,v)
        x.execute('commit')


i = Tk()
i.geometry('500x500')
i.title('prova')

l_nome = Label(i, text='Nome: ')
l_nome.place(x=50,y=50)
e_nome = Entry(i)
e_nome.place(x=130,y=50)

l_disciplina = Label(i, text='Disciplina: ')
l_disciplina.place(x=50, y=90)
e_disciplina = Entry(i)
e_disciplina.place(x=130, y=90)

l_nota = Label(i, text='Nota: ')
l_nota.place(x=50, y=130)
e_nota = Entry(i)
e_nota.place(x=130, y=130)

cadastrar = Button(i, text='Cadastrar Nota', command=cad)
cadastrar.place(x=150,y=180)

most = Button(i, text='Mostrar', command=mostrar)
most.place(x=270,y=180)

delet = Button(i, text='updt Nota', command=updt)
delet.place(x=400,y=180)

delet = Button(i, text='Deletar', command=deletar)
delet.place(x=335,y=180)

listbox = Listbox(i, width=50, height=17)
listbox.place(x=50,y=220)





i.mainloop()