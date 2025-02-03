def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def tabuada(a):
    contador = 1
    while contador <= 10:
        print(f"{a} X {contador} = {a*contador}")
        contador = contador + 1

def exibir_menu():
    print("\nEscolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Tabuada")
    print("6 - Sair")