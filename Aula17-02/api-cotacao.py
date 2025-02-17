import requests

def converter_dolar_para_real(dollar, dados):
    dollarReal = float(dados["USDBRL"]["bid"])
    return dollar * dollarReal

def converter_real_para_dolar(real, dados):
    dollarReal = float(dados["USDBRL"]["bid"])
    return real / dollarReal

def converter_dolar_para_bitcoin(dollar):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    dados = response.json()
    bitcoin_dollar = float(dados["bitcoin"]["usd"])
    return dollar / bitcoin_dollar

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
response = requests.get(url)
dados = response.json()

opcao = input("Você quer converter de (1) Dollar para Real, (2) Real para Dollar, ou (3) Dollar para Bitcoin? Digite 1, 2 ou 3: ")

if opcao == "1":
    userDollar = float(input("Digite um valor em Dollar para converter em Real: "))
    print("R$ ", converter_dolar_para_real(userDollar, dados))
elif opcao == "2":
    userReal = float(input("Digite um valor em Real para converter em Dollar: "))
    print("$ ", converter_real_para_dolar(userReal, dados))
elif opcao == "3":
    userDollar = float(input("Digite um valor em Dollar para converter em Bitcoin: "))
    print("₿ ", converter_dolar_para_bitcoin(userDollar))
else:
    print("Opção inválida")
