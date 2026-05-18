import pandas
#Pandas biblioteca para manipular dados tabulares.
#No Pandas uma planilha/tabela é chamado de DataFrame (Quadro de Dados)
#Um DataFrame é formado por um conjunto de Séries (Colunas)

#Vamos ler uma planilha de Excel e criar um DataFrame
df = pandas.read_excel("Planilha.xlsx")

#Imprimir a planilha
print(df)
#Imprime a linha que possui o índice 10
print(df.loc[10])
#Imprime apenas o valor que está na linha 10 - Coluna Nome
print(df.loc[10, "Nome"])

# loc(indice,coluna)
#Imprime apenas o valor que está na linha 10 nas Colunas:
#Nome e Peso
print (df.loc[10,("Nome", 'Peso')])

print(df.loc[:,"Nome"])
#Atualiza uma celua da tabela
df.loc[10,"Nome"] = "Outro Nome"
print(df)