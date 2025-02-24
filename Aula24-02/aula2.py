import csv

def obter_dados_usuarios():
    nome = input("Digite seu Nome: ")
    idade = input("Digite a sua idade: ")
    cidade = input("Digite sua Cidade: ")
    return [nome, idade, cidade]

def salvar_dados_no_csv(dados):
    with open('usuario.csv' ,mode='a' ,newline='' ,encoding='utf-8')as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(dados)
    print("Dados salvos com sucesso !")

def exibir_dados_csv():
    try:
        with open('usuarios.csv' , mode='r' ,newline='' ,encoding='utf-8')as arquivo:
            leitor = csv.reader(arquivo)
            print("\nDados armazenados com sucesso no csv")
            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        print("O arquivo ainda não foi criado")

while True:
    print("\nEscolha uma opção: ")
    print("1. Adicionar novo usuário ")
    print("2. Ver dados dos usuários ")
    print("3. Sair ")

    opcao = input("Digite um número de opção")
    if opcao=='1':
        dados_usuarios = obter_dados_usuarios()
        salvar_dados_no_csv(dados_usuarios)
    elif opcao=='2':
        exibir_dados_csv()
    elif opcao=='3':
        print("Fuiiiiiii...")
        break
    else:
        print("Opcao Invalida, Tente Novamente")