import funcao

#Como usar essas funções
funcao.imprimir('Digite um número 1: ')
n1 = funcao.lerInteiro()

funcao.imprimir('Digite um número 2: ')
n2 = funcao.lerInteiro()

r = funcao.somar(n1, n2)

funcao.pularLinha()
funcao.imprimir(f'O valor da soma de {n1} + {n2} é {r} ')
funcao.pularLinha()