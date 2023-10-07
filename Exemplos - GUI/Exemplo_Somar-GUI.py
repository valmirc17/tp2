# Exemplo  - Somar - GUI

"""
    Estrutura Fundamental do módulo Tkinter
    1º Importação da biblioteca
    2º Criação da GUI (Janela)
    3º Adicionar componentes(widgets) na janela(GUI)
    4º Evento loop
"""

from tkinter import *

# Função
def somar_numeros():
    num1 = float(txt_num1.get())
    num2 = float(txt_num2.get())
    resultado.set(num1+num2)

# Configuração da janela
janela = Tk()
janela.title("Cadastro de Clientes")

largura_janela = 400
altura_janela = 300

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

x = (largura_tela - largura_janela) // 2
y = (altura_tela - altura_janela) // 2

janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

fonte = ("Arial", 12)

# Frame para centralizar os itens na tela
tela = Frame(janela)
tela.pack(expand=True, padx=20, pady=20)

# Widgets (Exibição - Labels)
lbl_numero1 = Label(tela, text='Numero 1:',font=fonte)
lbl_numero1.pack()
txt_num1 = Entry(tela)
txt_num1.pack(pady=5)

lbl_numero2 = Label(tela, text='Numero 2:',font=fonte)
lbl_numero2.pack()
txt_num2 = Entry(tela)
txt_num2.pack(pady=5)

btn_somar = Button(tela, text='Somar',font=fonte,command=somar_numeros)
btn_somar.pack(pady=5)

# Exibir um conteúdo em formato String
resultado = StringVar()
lbl_resultado = Label(tela, textvariable=resultado,font=fonte)
lbl_resultado.pack(pady=5)


tela.mainloop()