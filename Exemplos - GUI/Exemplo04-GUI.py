# Exemplo 03 - GUI

from tkinter import *

tela = Tk()
tela.title('Fatec Registro')
tela.geometry('800x600')
tela.maxsize(width='800',height='600')
tela.minsize(width='400', height='300')

lbl_nome = Label(tela, text='Nome', font='Arial 20 bold italic', fg='#FF8C00').place (x=10, y=10)
lbl_cpf = Label(tela, text='CPF', font='Times 15 italic', fg='green').place (x=10,y=50)
tela.mainloop()