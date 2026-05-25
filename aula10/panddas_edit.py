# Pandas - Biblioteca de Manipulação de Dados Tabulares (Planilha)
# Pandas - semelhante a Banco de ados - DML

# Manipulação de dados (Inserir, Atualizar, Excluir e Consultar)

#instalar a lib: pip install pandas

#uso
import pandas as pd 

#criar a quadro de dados (DataFrame) equivalente a taabela no DB
#cria a variavel planilha que vai armazenar a planilha do excel
#que fi lida pelo pandas
planilha = pd.read_excel('Planilha.xlsx')


#vizualizar a planilha
print(planilha)
planilha.drop(['Carimbo de data/hora','Endereço de e-mail'], axis=1, inplace=True)

#inserir um registro na planilha
planilha.loc[len(planilha)]  = ['Ivan Paulino', 40, 'M', 85, 1.75]
print(planilha)

#inserir um registro na planilha
planilha.loc[len(planilha)]  = ['Izabel', 17, 'M', 78, 1.85]
print(planilha)

#atualizar apenas uma coluna
planilha.loc[19,'Idade'] =  25
print (planilha)

#atualizar duas ou mais colunas
planilha.loc[19,'Idade', 'Peso'] =  [25,2]
print (planilha)


#atualizar a linha inteira
planilha.loc [19] = ['Ivan Paulino', 40, 'M', 85, 1.75]
print(planilha)

#remover um registro da planilha
print('Removeu IVAN')
planilha_sem_ivan = planilha.drop(19)
print(planilha_sem_ivan)
print ('O Ivan ainda está aqui')
print (planilha)

print('A planilha tem', len(planilha), 'linhas')
