'''
Altere o código abaixo para que a condição que está dentro 
do else mude de lugar e fique dentro do if, mantendo a mesma funcionalidade

media = float(input('Digite sua média'))

if media >= 6:
    print('Aprovado')
else:
    if media > 3:
        print('Em exame final')
    else:
        print('Reprovado')
'''

media = float(input('Digite sua média'))

if media < 6 :
    if media < 3:
      print('Reprovado')
    else:
      print('Em exame final')
else:
    print('Aprovado')