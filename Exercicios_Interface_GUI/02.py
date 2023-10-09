# Exercício 02 - Velocidade Média

from tkinter import *

# Função
def calcular():
    deslocamento = float(txt_deslocamento.get())
    tempo = float(txt_tempo.get())
    resultado.set(deslocamento/tempo)

# Configuração da janela
janela = Tk()
janela.title("Velocidade média")

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
titulo = Label(tela, text="Velocidade média", font=("Arial", 18))
titulo.pack(pady=10)

lbl_deslocamento = Label(tela, text='Informe a variação de deslocamento (em metros):',font=fonte)
lbl_deslocamento.pack()
txt_deslocamento = Entry(tela)
txt_deslocamento.pack(pady=5)

lbl_tempo = Label(tela, text='Informe a variação do tempo percorrido (em segundos):',font=fonte)
lbl_tempo.pack()
txt_tempo = Entry(tela)
txt_tempo.pack(pady=5)

btn_calcular = Button(tela, text='Calcular',font=fonte,command=calcular)
btn_calcular.pack(pady=5)

# Exibir um conteúdo em formato String
resultado = StringVar()
lbl_resultado = Label(tela, textvariable=resultado,font=fonte)
lbl_resultado.pack(pady=5)

lbl_dev = Label(tela,text="Desenvolvido por Valmir - 2023")
lbl_dev.pack(pady=8)

tela.mainloop()
