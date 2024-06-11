import pandas as pd
import sqlite3
import os
from transforme import integrar_dados, processar_dados_movimentacao,tratar_dados_extraidos
from extract import buscar_todos_dados_commodities

commodities = ['CL=F', 'GC=F', 'SI=F']  # Petróleo bruto, Ouro, Prata

caminho_arquivo = ('data/movimentacao_commodities.csv')

def criaw_dw(df_integrado):
    os.makedirs('data/dw', exist_ok=True)
    conn = sqlite3.connect('data/dw/commodities_dw.db')
    df_integrado.to_sql('commodities', conn, if_exists='replace', index=False)
    conn.close()

if __name__ == "__main__":
    dados_de_todas_as_commodities = buscar_todos_dados_commodities(commodities)
    dados_tratados = tratar_dados_extraidos(dados_de_todas_as_commodities)
    dados_trados_do_csv = processar_dados_movimentacao(caminho_arquivo)
    dados_finais = integrar_dados(dados_tratados, dados_trados_do_csv)
    criaw_dw(dados_finais)
