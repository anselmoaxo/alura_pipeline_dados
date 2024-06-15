# Projeto de Aula: Introdução à Orientação a Objetos com Pipeline de Dados

Este projeto de aula visa introduzir o paradigma de orientação a objetos através da transformação de um pipeline de dados inicialmente implementado com funções em Python para uma estrutura orientada a objetos.

## Objetivos do Projeto

### Identificação da Necessidade de Orientação a Objetos

Compreender as limitações de um pipeline de dados baseado em funções soltas, especialmente quando há aumento na complexidade e necessidade de reutilização de código.

### Transformação para uma Classe

Refatorar o pipeline de dados para uma classe chamada `Dados`, que encapsula funcionalidades como carregar dados de diferentes fontes (JSON, CSV, lista em memória), processar esses dados e salvar resultados.

### Atributos e Métodos da Classe Dados

Definir atributos como `dados`, `nome_colunas` e `quantidade_linhas`. Implementar métodos para leitura de dados, renomear colunas, realizar junção de dados, transformar e salvar dados em um formato final.

### Refatoração para Novas Necessidades

Adicionar novos métodos ou ajustar os existentes conforme novas funcionalidades ou requisitos do pipeline de dados.

### Utilização do Pipeline de Dados em Script

Criar um script (`processamento_dados.py`) que demonstra a utilização da classe `Dados`, incluindo a carga de dados, processamento e salvamento dos resultados.

## Uso do Projeto

Para utilizar este projeto em seu ambiente de desenvolvimento:

1. Clone este repositório para sua máquina local.
2. Explore os arquivos para entender a estrutura do projeto.
3. Execute o script `processamento_dados.py` para ver a classe `Dados` em ação.

