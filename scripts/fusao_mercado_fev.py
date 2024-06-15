from processamento_dados import Dados 
        
#Path                
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'
path_dados_combinados = 'data_processed/dados_combinados.csv'

#Extract

print('***Extração dos Dados Empresa A - Empresa B***')
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


#Transform

print('***Transformação dos Dados Empresa A - Empresa B***')
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


#Load
print('---------------------------------------------')
print('***Salvando Arquivo da fusão***')
dados_fusao.salvando_dados_fusao(path_dados_combinados)
print('---------------------------------------------')
print(f'Dados salvo com sucesso em : {path_dados_combinados}')