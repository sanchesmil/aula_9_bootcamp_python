import pandas as pd
import os
import glob

from log_decorator import log_decorator

# funcao que lê e consolida arquivos json
@log_decorator
def extrair_dados_e_consolidar(path_pasta:str)->pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path_pasta,'*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

# funcao que transforma os dados
@log_decorator
def calcular_kpi_total_vendas(df:pd.DataFrame)->pd.DataFrame:
    df['Total'] = df['Quantidade'] * df['Venda']
    return df

@log_decorator
def carregar_dados(df:pd.DataFrame,formato_saida: list):
    """Parâmetro será CSV ou PARQUET ou os dois"""
    for formato in formato_saida:
        if formato == 'csv':
            df.to_csv('dados.csv', index=False)
        if formato == 'parquet':
            df.to_parquet('dados.parquet', index=False)

@log_decorator
def pipeline_calcular_kpi_vendas_consolidada(path_pasta:str, formato_saida:list ):
    df_consolidado = extrair_dados_e_consolidar(path_pasta)
    df_transformado = calcular_kpi_total_vendas(df_consolidado)
    carregar_dados(df_transformado, formato_saida)