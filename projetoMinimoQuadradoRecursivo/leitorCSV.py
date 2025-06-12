import pandas as pd

def carregar_csv_para_dicionario(caminho_arquivo_csv: str, lista_nomes_colunas_desejadas: list = None) -> dict | None:
    try:

        data_dados_lidos = pd.read_csv(caminho_arquivo_csv)
        print(f"Arquivo {caminho_arquivo_csv} lido com sucesso. Colunas disponíveis: {data_dados_lidos.columns.tolist()}")

        dados_extraidos = {}

        for nome_coluna in lista_nomes_colunas_desejadas:
            if nome_coluna in data_dados_lidos.columns:
                dados_extraidos[nome_coluna] = data_dados_lidos[nome_coluna]

            if not dados_extraidos:
                print(f"Nenhuma coluna em {lista_nomes_colunas_desejadas} foi encontrada no arquivo CSV")

    
    except FileNotFoundError:
        print(f"ERRO: O arquivo '{caminho_arquivo_csv}' não foi encontrado. Verifique o caminho e o nome do arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo CSV: {e}")
        return {}
    
    return dados_extraidos