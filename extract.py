import yfinance as yf
import pandas as pd
from loguru import logger
import time

start_time = time.time()
commodities = ['CL=F', 'GC=F', 'SI=F']  # Petróleo bruto, Ouro, Prata
logger.add("file_{time}.log")

def buscar_dados_commodities(simbolo, periodo='5d', intervalo='1d'):
    """
    recebe um parametro e retorna o preco dessas acoes
    """
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period=periodo, interval=intervalo)
    dados['simbolo'] = simbolo  # Adiciona a coluna do símbolo
    return dados
    
def buscar_todos_dados_commodities(commodities):
    """
    cancatena todos os precos de acoes
    """
    todos_dados = []
    for simbulo in commodities:
         dados_de_commodities = buscar_dados_commodities(simbulo)
         todos_dados.append(dados_de_commodities)
    return pd.concat(todos_dados)

if __name__ == "__main__":
    dados_de_todas_as_commodities = buscar_todos_dados_commodities(commodities)
    