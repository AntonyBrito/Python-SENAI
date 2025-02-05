cadastros = {}

def cadastro():
    nome = input("Digite o nome do novo cadastro: ")
    if nome in cadastros:
        print("Cadastro já existe")
    else:
        idade = int(input(f"Digite a idade de {nome}: "))
        cadastro[nome] = idade
        print(f"Cadastro de {nome} realziado com sucesso!")

def excluir_cadastro():
    nome = input("Digite o nome para excluir")
    if nome in cadastros:
        del cadastros[nome]
        print("Cadastro excluído com sucesso!")
    else:
        print("Cadastro não encontrado")

def mostrar_cadastro():
    if cadastros:
        print("Lista de cadastros: \n")
        for nome, idade in cadastros.items():
            print(f"Nome: {nome}, Idade: {idade}")
    else:
        print("Não existe cadastro registrado")

def menu():
    while True:
        print("1 - Incluir Cadastro")
        print("2 - Excluir Cadastro")
        print("3 - Mostrar Cadastro")
        print("4 - Sair")
        opcao = input("Escolher opção")

        match opcao:
            case "1":
                cadastro()
            case "2":
                excluir_cadastro()
            case "3":
                mostrar_cadastro()
            case "4":
                print("Saindo...")
                break
            case _:
                print("Opção inválida")

menu()