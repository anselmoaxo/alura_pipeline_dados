import json
import csv

class Dados:
    
    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        self.nome_colunas = self.get_columns()
        self.quantidade_linhas = self.size_data()
        
    def leitura_json(self):
        dados_json = []
        with open(self.path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

    def leitura_csv(self):
        dados_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    def leitura_dados(self):
        if self.tipo_dados == 'json':
            dados_json = self.leitura_json()
            return dados_json
        
        elif self.tipo_dados == 'csv':
            dados_csv = self.leitura_csv()
            return dados_csv
        
        elif self.tipo_dados == 'list':
            dados = self.path
            self.path = 'Lista em memoria'
            return dados
        
    def get_columns(self):
        return list(self.dados[-1].keys())
    
      
    def rename_columns(self, key_mapping):
        new_dados = []

        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)
            
        self.dados = new_dados
        self.nome_colunas = self.get_columns()
    
    def size_data(self):
        return len(self.dados)
    
    
    def join(dadosA, dadosB):
        combined_list = []
        combined_list.extend(dadosA.dados)
        combined_list.extend(dadosB.dados)
        return Dados(combined_list, 'list')
    
    def transformando_dados_tabela(self):
        dados_combinados_tabela = [self.nomes_colunas]

        for row in self.dados:
            linha =  []
            for coluna in nomes_colunas:
                linha.append(row.get(coluna, 'Indisponivel'))
            dados_combinados_tabela.append(linha) 
        return dados_combinados_tabela
        
    
        