import cadastroCliente

lista = []

opcaoMenu = True
while opcaoMenu == True:
    opcao = input(f"Digite uma opção: \n1 - Adicionar usúario \n2- Listar usíarios \n3- Excluir usúarios \n4 - Sair")

    match opcao:
        case "1":
            cadastroCliente.adicionar(lista)
        case "2":
            cadastroCliente.listar(lista)
        case "3":
            cadastroCliente.excluir(lista)   
        case "4":
            opcaoMenu = False
            break