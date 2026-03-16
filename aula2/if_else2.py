media = float(input('Digite sua média'))

if media >= 6:
    print('Aprovado')
else:
    if media > 3:
        print('Em exame final')
    else:
        print('Reprovado')