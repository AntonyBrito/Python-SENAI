import tkinter as tk
import requests

def converter():
    try:
        # Obtém o valor em reais (BRL) inserido pelo usuário
        valor_reais = float(entrada_valor.get())
        
        # Faz a requisição para a API de cotações
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        resposta = requests.get(url)
        dados = resposta.json()
        
        # Obtém a cotação do dólar
        cotacao_dolar = float(dados["USDBRL"]["bid"])
        
        # Converte para dólares (USD)
        valor_dolares = valor_reais / cotacao_dolar
        
        # Atualiza o rótulo com o resultado formatado
        resultado.config(text=f"USD: ${valor_dolares:.2f}")
    except ValueError:
        resultado.config(text="Por favor, insira um número válido.")
    except Exception as e:
        resultado.config(text="Erro ao acessar a API.")

# Configuração da interface Tkinter
janela = tk.Tk()
janela.title("Conversor BRL → USD")

# Campo de entrada
tk.Label(janela, text="Valor em R$:", font=("Arial", 12)).pack(padx=10, pady=5)
entrada_valor = tk.Entry(janela, font=("Arial", 12))
entrada_valor.pack(padx=10, pady=5)

# Botão de conversão
botao_converter = tk.Button(janela, text="Converter", command=converter, font=("Arial", 12))
botao_converter.pack(padx=10, pady=10)

# Rótulo do resultado
resultado = tk.Label(janela, text="USD: $0.00", font=("Arial", 14, "bold"))
resultado.pack(padx=10, pady=10)

# Executa a interface gráfica
janela.mainloop()