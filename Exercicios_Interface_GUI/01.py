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
def calcular():
    altura_cm = float(txt_altura.get())
    resultado.set(altura_cm*100)

# Configuração da janela
janela = Tk()
janela.title("Conversão de estatura")

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
titulo = Label(tela, text="Conversão de estatura", font=("Arial", 18))
titulo.pack(pady=10)

lbl_altura = Label(tela, text='Informe sua estatura (em metros):',font=fonte)
lbl_altura.pack()
txt_altura = Entry(tela)
txt_altura.pack(pady=5)

btn_calcular = Button(tela, text='Calcular',font=fonte,command=calcular)
btn_calcular.pack(pady=5)

# Exibir um conteúdo em formato String
resultado = StringVar()
lbl_resultado = Label(tela, textvariable=resultado,font=fonte)
lbl_resultado.pack(pady=5)


tela.mainloop()