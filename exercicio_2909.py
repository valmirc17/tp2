import tkinter as tk
import json


def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    endereco = entry_endereco.get()

    # resultado.config(text=f"Nome: {nome}\nEmail: {email}\nTelefone: {telefone}\nEndereço: {endereco}")
    dados = {
        'nome': nome,
        'email': email,
        'telefone': telefone,
        'endereco': endereco
    }

    # Converta o dicionário em JSON
    resultado_json = json.dumps(dados)

    # Agora você pode usar dados_json conforme necessário
    resultado.config(text=resultado_json)



janela = tk.Tk()
janela.title("Cadastro de Clientes")

largura_janela = 800
altura_janela = 600

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

x = (largura_tela - largura_janela) // 2
y = (altura_tela - altura_janela) // 2

janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

fonte = ("Arial", 12)

frame = tk.Frame(janela)
frame.pack(expand=True, padx=20, pady=20)

titulo = tk.Label(frame, text="Cadastro de Clientes", font=("Arial", 18))
titulo.pack(pady=10)

label_nome = tk.Label(frame, text="Nome:", font=fonte)
label_nome.pack()
entry_nome = tk.Entry(frame, font=fonte)
entry_nome.pack(pady=5)

label_email = tk.Label(frame, text="Email:", font=fonte)
label_email.pack()
entry_email = tk.Entry(frame, font=fonte)
entry_email.pack(pady=5)

label_telefone = tk.Label(frame, text="Telefone:", font=fonte)
label_telefone.pack()
entry_telefone = tk.Entry(frame, font=fonte)
entry_telefone.pack(pady=5)

label_endereco = tk.Label(frame, text="Endereço:", font=fonte)
label_endereco.pack()
entry_endereco = tk.Entry(frame, font=fonte)
entry_endereco.pack(pady=10)

botao_cadastrar = tk.Button(frame, text="Cadastrar", font=fonte, command=cadastrar)
botao_cadastrar.pack()

resultado = tk.Label(frame, text="", font=fonte)
resultado.pack(pady=10)

rodape = tk.Label(janela, text="Desenvolvido por Valmir - 2023", font=("Arial", 10, ), anchor="se")
rodape.pack(side="bottom", padx=10, pady=10, fill="both")

janela.mainloop()
