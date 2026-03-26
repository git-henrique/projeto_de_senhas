import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import base64
import os 


# O arquivo cofre.dat é ignorado pelo Git por conter dados sensíveis.
# Use o cofre.exemplo.dat como referência :)
ARQUIVO = "cofre.dat"

# Função simples de "criptografia"
def criptografar(texto):
    return base64.b64encode(texto.encode()).decode()

def descriptografar(texto):
    return base64.b64decode(texto.encode()).decode()

# Carregar dados
def carregar():
    if not os.path.exists(ARQUIVO): 
        return {}
    with open(ARQUIVO, 'r') as f:
        return json.load(f)
    
# Salvar dados (senhas)
def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f)

# Tela principal
def abrir_cofre():
    dados = carregar()

    def adicionar():
        site = simpledialog.askstring('Site', 'Digite o nome do site: ')
        usuario = simpledialog.askstring('Usuario', 'Digite o usuario: ')
        senha = simpledialog.askstring('Senha', 'Digite a senha: ')

        if site and usuario and senha:
            dados[site] = {
                'usuario': usuario,
                'senha': criptografar(senha)
            }
            salvar_dados(dados)
            atualizar_lista()

    def ver():
        selecionado = lista.get(tk.ACTIVE)
        if selecionado:
            info = dados[selecionado]
            usuario = info['usuario']
            senha = descriptografar(info['senha'])
            messagebox.showinfo('Dados', f"Usuário: {usuario}\n Senha: {senha}")

    def atualizar_senha():
        if not lista.curselection():
            messagebox.showwarning('Aviso', "Selecione um site primeiro!")
            return
        
        selecionado = lista.get(tk.ACTIVE) 
        info = dados[selecionado]
        nova_senha = simpledialog.askstring("Senha", 'Digite a nova senha: ')
        
        if nova_senha:
            dados[selecionado] = {
                'usuario': info['usuario'],
                'senha': criptografar(nova_senha)
            }
            salvar_dados(dados)
            atualizar_lista() 
            messagebox.showinfo('Sucesso', "Senha atualizada com sucesso!")


    def atualizar_lista():
        lista.delete(0, tk.END)
        for site in dados:
            lista.insert(tk.END, site)

    janela = tk.Tk()
    janela.title("Cofre de Senhas")

    lista = tk.Listbox(janela, width=40)
    lista.pack()

    btn_add = tk.Button(janela, text="Adicionar", command=adicionar)
    btn_add.pack()

    btn_ver = tk.Button(janela, text="Ver senha", command=ver)
    btn_ver.pack()

    btn_atualizar = tk.Button(janela, text="Atualizar Senha", command=atualizar_senha)
    btn_atualizar.pack()

    atualizar_lista()
    janela.mainloop()

# Tela de Login
def login():
    root = tk.Tk()
    root.withdraw()

    senha = simpledialog.askstring('Login', "Digite a senha mestre: ", show="*")

    if senha == "senhaDificilparaTestar":
        abrir_cofre()
    else:
        messagebox.showerror('Erro', "Senha mestre incorreta!")

login()
