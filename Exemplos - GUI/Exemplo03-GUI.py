# Exemplo 01 - GUI

# Importação da biblioteca

from tkinter import *

# Tela invoca função Tk
tela = Tk()

# Título na barra de tarefas
tela.title('Fatec Registro')

# Configuração da cor de tela (opcional)
tela.configure(background='#1a1a1a')

# Configuração do tamanho da tela
tela.geometry('800x600')

# Configuração de limite da tela

tela.resizable(True,True)

# Tamanho máximo
tela.maxsize(width=800,height=600)

# Tamanho mínimo
tela.minsize(width=400,height=300)

# Criando um componente
lbl_teste = Label(tela,text='Teste',font='Calibri',background='green',).place (x=400,y=300)


tela.mainloop()