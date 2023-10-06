# Exemplo 04 - GUI

from tkinter import *

tela = Tk()
tela.title('Fatec Registro')

# Dimensões da tela
largura = 800
altura = 600

#Resolução do sistema(tela)
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

#Definição do posicionamento
posx = largura_screen / 2 - largura/2
posy = altura_screen / 2 - altura/2

# Visualização do tamanho da tela no terminal
print(largura_screen, altura_screen)

# Definição do geometry
tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
tela.mainloop()