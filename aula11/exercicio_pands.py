import pandas as pd

# 1. Leitura de Dados

df_notas = pd.read_excel("notas_estudantes.xlsx", sheet_name= "Notas")
df_atividades = pd.read_excel("notas_estudantes.xlsx", sheet_name= "Atividades")

print(df_notas)
print(df_atividades)

#2. Inserção de Registro

df_notas.loc[len(df_notas)]  = ['Lucas Silva', 'Prova Final',  8.5]
print(df_notas)

#3. Atualização de Dados
#v1

df_notas.loc[1, "Nota"]  = 9 #Na linha 1 na coluna Nota coloca o valor 9
print(df_notas)

#v2

condicao1= df_notas['Nome'] == 'Ana Souza'
condicao2= df_notas['Atividade'] == 'Trabalho 1'
#seleciona a linha usando condições
df_notas.loc[condicao1 & condicao2, "Nota"]  = 9 
print(df_notas)

#4. Exclusão de Registro
#v1
df_notas.drop(2, inplace=True)
print(df_notas)

#v2
condicao1 = df_notas['Nome'] == 'Pedro Santos'
condicao2 = df_notas['Atividade'] == 'Prova 1'
resposta = df_notas.loc[condicao1 & condicao2]
df_notas.drop(resposta.index, inplace=True)
print(resposta)

#5. Filtragem Simples
condicao2 = df_notas ['Nota'] > 7
resposta = df_notas.loc[condicao1]
print (resposta)

#6. Agrupamento e Agregação
resposta= df_notas.groupby('Nome')['Nota'].mean()
print(resposta)

#7. Projeção de Colunas
print(df_notas.loc[:, ['Nome','Nota']])

#8. Filtragem por Texto
condicao1 = df_notas['Atividade'] == 'Prova Final'
resposta = df_notas.loc[condicao1]
print (resposta)

#9. Filtragem Composta e Projeção
condicao1 = df_notas['Nota'] > 7
condicao2 = df_notas['Atividade'] == 'Prova Final'
resposta = df_notas.loc[condicao1 & condicao2, ('Nome', 'Nota')]
print (resposta)

#10. Ordenação
resposta = df_notas.sort_values('Nome', ascending=True)
print(resposta)

#11. Junção de DataFrames (Merge)
nova_planilha = pd.merge(df_notas, df_atividades, on= 'Atividade', how= "inner")
print(nova_planilha)

#12. Exportação de Dados
df_notas.to_excel('PlanilhaNova.xlsx', index=False)