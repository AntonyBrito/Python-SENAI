def adicionar(list):
    list.append(input("Digite o nome do usúario para adicionar"))

def listar(list):
    print(list)

def excluir(list):
    print("Digite o número do usúario que você deseja excluir: ")
    for nome in list:
        contador = 1
        print(f"{contador} -", nome)
        contador = contador + 1

    excluirUser = int(input(""))
    list.pop[excluirUser]
    
        

    
    