import csv
import tkinter as tK
from tkinter import messagebox

#função para pedir dados do usuários
def obter_dados_usuario():
    nome = entry_nome.get()
    idade = entry_idade.get()
    cidade = entry_cidade.get()
    return[nome, idade, cidade]

#função para salvar dados em csv
def salvar_dados_no_csv(dados):
    with open("usuarios.csv", mode='a', newline='', encoding='utf-8')as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(dados)
    messagebox.showinfo("Sucesso", "Dados salvos com sucesso")

#função para ler e exibir os dados do csv
def exibir_dados_csv():
    try:
        with open('usuarios.csv', mode='r', newline='', encoding='utf-8')as arquivo:
            leitor=csv.reader(arquivo)
            dados_texto.delete(1.0,tK.END)
            for linha in leitor:
                dados_texto.insert(tK.END,f"Nome: {linha[0]}, Idade: {linha[1]}, Cidade: {linha[2]}\n")
    except FileNotFoundError:
        messagebox.showerror("Erro", "O arquivo ainda não foi criado")
#função para limpar campos
def limpar_campos():
    entry_nome.delete(0,tK.END)
    entry_idade.delete(0,tK.END)
    entry_cidade.delete(0,tK.END)

#configuração da janela principal
root=tK.Tk()
root.title("Cadastro de Usuários...")

#Labels e campos de entrada
label_nome = tK.Label(root, text="Nome: ")
label_nome.pack()
entry_nome = tK.Entry(root)
entry_nome.pack()

label_idade = tK.Label(root, text="Idade: ")
label_idade.pack()
entry_idade = tK.Entry(root)
entry_idade.pack()

label_cidade = tK.Label(root, text="Cidade: ")
label_cidade.pack()
entry_cidade = tK.Entry(root)
entry_cidade.pack()

#Botoes de ações
botao_adicionar = tK.Button(root, text='Adicionar Usuários', command=lambda:
salvar_dados_no_csv(obter_dados_usuario()))
botao_adicionar.pack()

botao_exibir = tK.Button(root, text="Ver dados do Usuário", command=exibir_dados_csv)
botao_exibir.pack()

botao_limpar = tK.Button(root, text="Limpar Campos", command=limpar_campos)
botao_limpar.pack()

#Area de exibição
dados_texto = tK.Text(root, height=10, width=50)
dados_texto.pack()

#Rodar a interface grafica
root.mainloop()