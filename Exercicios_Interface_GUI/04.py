# Exercício 04 - Área do triângulo
from tkinter import *
from math import pi
# Função
def calcular():
    base = float(txt_base.get())
    alt = float(txt_alt.get())
    resultado.set((base*alt)/2)

# Configuração da janela
janela = Tk()
janela.title("Área do triângulo")

largura_janela = 400
altura_janela = 300

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

x = (largura_tela - largura_janela) // 2
y = (altura_tela - altura_janela) // 2

janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

fonte = ("Arial", 11)

# Frame para centralizar os itens na tela
tela = Frame(janela)
tela.pack(expand=True, padx=20, pady=20)


# Widgets (Exibição - Labels)
titulo = Label(tela, text="Área do triângulo", font=("Arial", 18))
titulo.pack(pady=10)

lbl_base = Label(tela, text='Informe a base:',font=fonte)
lbl_base.pack()
txt_base = Entry(tela)
txt_base.pack(pady=5)

lbl_alt = Label(tela, text='Informe a altura:',font=fonte)
lbl_alt.pack()
txt_alt = Entry(tela)
txt_alt.pack(pady=5)


btn_calcular = Button(tela, text='Calcular',font=fonte,command=calcular)
btn_calcular.pack(pady=5)

# Exibir um conteúdo em formato String
resultado = StringVar()
lbl_resultado = Label(tela, textvariable=resultado,font=fonte)
lbl_resultado.pack(pady=5)

lbl_dev = Label(tela,text="Desenvolvido por Valmir - 2023")
lbl_dev.pack(pady=8)

tela.mainloop()
