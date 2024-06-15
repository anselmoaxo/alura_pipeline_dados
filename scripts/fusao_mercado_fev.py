import json
import csv
from processamento_dados import Dados

    
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

#Extract
print('---------------------------------------------')
print('Extração dos Dados Empresa A - Empresa B')
print('---------------------------------------------')
dados_empresaA = Dados(path_json, 'json')
dados_empresaB = Dados(path_csv, 'csv')

print(f' Dados da Empresa A {dados_empresaA.dados[0]}')
print(f'Quantidade de Linhas dos Dados da EmpresaA : {dados_empresaA.quantidade_linhas}')
print('---------------------------------------------')
print(f' Dados da Empresa B {dados_empresaB.dados[0]}')
print(f'Quantidade de Linhas dos Dados da EmpresaB : {dados_empresaB.quantidade_linhas}')
print('---------------------------------------------')
print(f'Colunas Empresa A {dados_empresaA.nome_colunas}')
print('---------------------------------------------')
print(f'Colunas Empresa B {dados_empresaB.nome_colunas}')
print('---------------------------------------------')


#transformação do dados
print('---------------------------------------------')
print('Transformação dos Dados Empresa A - Empresa B')
print('---------------------------------------------')
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}


dados_empresaB.rename_columns(key_mapping)
print(f'Colunas Renomeadas  {dados_empresaB.nome_colunas}')
print('---------------------------------------------')

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)

print(f'Colunas Fusão{dados_fusao.nome_colunas}')
print('---------------------------------------------')
print(f'Quantidade de Linhas dos Dados da EmpresaA : {dados_empresaA.quantidade_linhas}')
print('---------------------------------------------')
print(f'Quantidade de Linhas dos Dados da EmpresaB : {dados_empresaB.quantidade_linhas}')
print('---------------------------------------------')
print(f'Quantidade de Linhas dos Dados da Fusao : {dados_fusao.quantidade_linhas}')


# salvando dados
#dados_fusao_tabela = transformando_dados_tabela(dados_fusao, nome_colunas_fusao)

#salvando_dados_fusao(path_dados_combinados, dados_fusao_tabela)
#print(path_dados_combinados)