#Estrutura de repetição For: 
#Percorrer listas
#Lista estrutura de dados composta (armazena diversos valores)
#Variável que possui vários valores

nomes = ['Pietro', 'Ryan', 'Maria', 'Gabriela', 'Sophia']

#imprime toda a lista (conjunto)
print(nomes)

#imprime um nome individualmente (Maria)
print(nomes[2])


#imprime todos os nomes da lista utilizando for - range
for i in range(5):
    print(nomes[i])

#outra opção para interar (percorrer de 1 em 1) sobre as listas
for nome in nomes:
    print(nome)
