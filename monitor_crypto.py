import requests
import pandas as pd
from datetime import datetime
import time

def extrair_dados():
    # Coleta o preço do Bitcoin em Reais
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl"
    response = requests.get(url)
    return response.json()['bitcoin']['brl']

def transformar(preco):
    # Organiza os dados em um formato de tabela
    return {
        "Moeda": "Bitcoin",
        "Preço (R$)": preco,
        "Data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

# --- Execução ---
historico = []
print("Iniciando ETL... Coletando dados (3 ciclos)")

for i in range(3):
    preco_atual = extrair_dados()
    dados_tratados = transformar(preco_atual)
    historico.append(dados_tratados)
    print(f"Check {i+1}: R$ {preco_atual}")
    if i < 2: time.sleep(5) # Espera 5 segundos

# CARGA: Salva tudo no Excel/CSV
df = pd.DataFrame(historico)
df.to_csv("relatorio_cripto.csv", index=False)
print("\n✅ Sucesso! O arquivo 'relatorio_cripto.csv' foi criado.")
