from tkinter import *
from tkinter import messagebox
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="q1"
)

x = conexao.cursor()

#x.execute('create database q1')

#x.execute('create table aluno(id int primary key auto_increment, nome varchar(30), disciplina varchar(30), nota float)')

def inserir():
    nome = enome.get()
    disciplina = edisciplina.get()
    nota = enota.get()

    if any(f=='' for f in [nome,disciplina,nota]):
        messagebox.showinfo('ERRO','CAMPOS EM BRANCO')
    else:
        a = 'insert into aluno(nome,disciplina,nota) values(%s,%s,%s)'
        v = (nome,disciplina,nota)
        x.execute(a,v)
        x.execute('commit')
        messagebox.showinfo('SUCESSO','CADASTRADOM COM SUCESSO')

        for i in [enome,edisciplina,enota]:
            i.delete(0,END)

        b = 'select * from aluno where nota > 7.0'
        x.execute(b)
        r = x.fetchall()
        x.execute('commit')
        lista.delete(0,END)
        for row in r:
            lista.insert(END, ' '.join(map(str,row)))

def up():
    nome = enome.get()

    if nome == "":
        messagebox.showinfo('erro','CAMPO VAZIO')
    else:
        k = 'update aluno set nota = NULL where nome = %s'
        m = (nome,)
        x.execute(k,m)
        x.execute('commit')

        messagebox.showinfo('SUCESSO','NOTA ALTERADA')

    

i = Tk()
i.geometry('500x500')
i.title('q1')

lnome = Label(i, text='Nome: ')
lnome.place(x=10,y=20)
enome = Entry(i)
enome.place(x=100, y=20)

ldisciplina = Label(i, text='Disciplina: ')
ldisciplina.place(x=10, y=50)
edisciplina = Entry(i)
edisciplina.place(x=100, y=50)

lnota = Label(i,text='Nota: ')
lnota.place(x=10,y=80)
enota=Entry(i)
enota.place(x=100,y=80)

btn = Button(i,text='Cadastrar Nota', command=inserir)
btn.place(x=100,y=110)

btn = Button(i,text='Up nota', command=up)
btn.place(x=200,y=110)

lista = Listbox(i,width=70,height=20)
lista.place(x=10,y=150)


i.mainloop()