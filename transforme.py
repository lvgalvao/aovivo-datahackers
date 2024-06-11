import pandas as pd
from extract import buscar_todos_dados_commodities

commodities = ['CL=F', 'GC=F', 'SI=F']  # Petróleo bruto, Ouro, Prata

caminho_arquivo = ('data/movimentacao_commodities.csv')

def tratar_dados_extraidos(dados: pd.DataFrame) -> pd.DataFrame:
    dados = dados.rename(columns={'Date':'data'})
    dados = dados.rename(columns={'Close': 'fechamento'})
    dados['data'] = pd.to_datetime(dados.index, utc=True).date
    return dados.reset_index(drop=True)

def processar_dados_movimentacao(caminho: str):
    df = pd.read_csv(caminho)
    df['date'] = pd.to_datetime(df['date']).dt.date
    df = df.rename(columns={'date': 'data','symbol': 'simbolo'})
    return df

def integrar_dados(dados_commodities, df_movimentacao):
    df_final = dados_commodities.merge(df_movimentacao, on=['data', 'simbolo'], how='inner') 
    df_final['valor'] = df_final['quantity'] * df_final['fechamento']
    df_final['ganho'] = df_final.apply(
        lambda row: row['valor'] if row['action'] == 'sell' else -row['valor'], axis=1
    )
    return df_final
    
    pass

if __name__ == "__main__":
    dados_de_todas_as_commodities = buscar_todos_dados_commodities(commodities)
    dados_tratados = tratar_dados_extraidos(dados_de_todas_as_commodities)
    
    dados_trados_do_csv = processar_dados_movimentacao(caminho_arquivo)

    dados_finais = integrar_dados(dados_tratados, dados_trados_do_csv)
    print(dados_finais)