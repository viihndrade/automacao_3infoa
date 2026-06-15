import pandas as pd # AS PD significa que mudei o nome "pandas" para "pd"

tabela = pd.read_excel("aula 11\\dados.xlsx", sheet_name= "alunos") # PD.READ lê a tabela, e o SHEET_NAME serve para ler uma "categoria" diferente e queremos ler apenas um

print (tabela)

print (tabela.head(5)) #.HEAD serve para printar os 5 PRIMEIROS
print (tabela.tail(5)) #.TAIL serve para printar os 5 ULTIMOS

tabela.loc[len(tabela)] = [8, 'enzo', 'tecnico em jogos', 'TGA'] # serve para localizar uma linha na tabela, caso uma tabela tenha 5 linhas , e pedimos para localizar a linha 6, ele vai CRIAR uma nova linha na tabela, mas também podemos usar essa linha de codigo para MODIFICAR um alinha na tabela
print (tabela)

tabela.loc[5, "nome"] = "joão" #ele serve para modificar uma coluna em especifica de determinada linha

tabela.drop(1, inplace=True) #.DROP serve para EXCLUIR, e o INPLACE serve para excluir um item dentro da propria tabela

calssificadores = tabela.sort_values('nome', ascending=True ) #serve para classificar em ordem, se o ASCENDING for true ent será cresecente, se for false sera decrescente

tabela.groupby('curso').count() #GROUPBY serve para grupar, e o COUNT serve para CONTAR, podemos usar ao inves do COUNT o MIN e MAX

tabela.value_counts('turma') #serve para printar um valor especifico

#EXPORTA DIRETO PARA A TABELA EXCEL
#nome da variavel a ser salva#'.to_excel