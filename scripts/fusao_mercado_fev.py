import json
import csv


def leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json

def leitura_csv(path_csv):
    dados_csv = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)
    return dados_csv

def leitura_dados(path, tipo_arquivo):
    if tipo_arquivo == 'json':
        dados_json = leitura_json(path_json)
        return dados_json
    elif tipo_arquivo == 'csv':
        dados_csv = leitura_csv(path_csv)
        return dados_csv
    
def get_columns(dados):
    return list(dados[-1].keys())
    
def rename_columns(dados, key_mapping):
    new_dados_csv = []

    for old_dict in dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados_csv.append(dict_temp)
    return new_dados_csv

def join(dados_empresaA, dados_empresaB):
    combined_list = []
    combined_list.extend(dados_empresaA)
    combined_list.extend(dados_empresaB)
    return combined_list
    
def transformando_dados_tabela(dados, nomes_colunas):
    dados_combinados_tabela = [nomes_colunas]

    for row in dados:
        linha =  []
        for coluna in nomes_colunas:
            linha.append(row.get(coluna, 'Indisponivel'))
        dados_combinados_tabela.append(linha) 
    return dados_combinados_tabela
  
def salvando_dados_fusao(path, dados_fusao):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados_fusao)
  
        
#Caminhos                
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'
path_dados_combinados = 'data_processed/dados_combinados.csv'


# Inciando a Leitura
dados_json = leitura_dados(path_json, 'json')
print(f'Dados Json {dados_json[0]}')

dados_csv = leitura_dados(path_csv, 'csv')
print(f'Dados CSV {dados_csv[0]}')

nome_colunas_json = get_columns(dados_json)
nome_colunas_csv = get_columns(dados_csv)

print(f'Colunas JSON {nome_colunas_json}')
print(f'Colunas CSV {nome_colunas_csv}')


#transformação do dados
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}


dados_csv = rename_columns(dados_csv, key_mapping)
nome_colunas_csv = get_columns(dados_csv)
print(f'Colunas Renomeadas CSV {nome_colunas_csv}')

dados_fusao = join(dados_json,dados_csv)
nome_colunas_fusao = get_columns(dados_fusao)
print(nome_colunas_fusao)


# salvando dados
dados_fusao_tabela = transformando_dados_tabela(dados_fusao, nome_colunas_fusao)

salvando_dados_fusao(path_dados_combinados, dados_fusao_tabela)
print(path_dados_combinados)