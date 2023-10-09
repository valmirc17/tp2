# Exercício 03 - Área de convivência
from tkinter import *
from math import pi
# Função
def calcular():
    raio = float(txt_raio.get())
    resultado.set(pi*raio**2)

# Configuração da janela
janela = Tk()
janela.title("Área de convivência")

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
titulo = Label(tela, text="Área de convivência", font=("Arial", 18))
titulo.pack(pady=10)

lbl_raio = Label(tela, text='Informe o raio da área de convivência:',font=fonte)
lbl_raio.pack()
txt_raio = Entry(tela)
txt_raio.pack(pady=5)


btn_calcular = Button(tela, text='Calcular',font=fonte,command=calcular)
btn_calcular.pack(pady=5)

# Exibir um conteúdo em formato String
resultado = StringVar()
lbl_resultado = Label(tela, textvariable=resultado,font=fonte)
lbl_resultado.pack(pady=5)

lbl_dev = Label(tela,text="Desenvolvido por Valmir - 2023")
lbl_dev.pack(pady=8)

tela.mainloop()
