import calculadora

def main():
    while True:
        calculadora.exibir_menu()
        escolha = input("Digite o número da operação: ")
        
        if escolha == '1':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = calculadora.soma(a, b)
            print(f"O resultado da soma é: {resultado}")
        
        elif escolha == '2':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = calculadora.subtracao(a, b)
            print(f"O resultado da subtração é: {resultado}")
        
        elif escolha == '3':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = calculadora.multiplicacao(a, b)
            print(f"O resultado da multiplicação é: {resultado}")
        
        elif escolha == '4':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = calculadora.divisao(a, b)
            print(f"O resultado da divisão é: {resultado}")

        elif escolha == '5':
            a = float(input("Digite um número: "))
            calculadora.tabuada(a)
        
        elif escolha == '6':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

main()