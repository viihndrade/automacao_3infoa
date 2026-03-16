
#Entrada
título = input('Digite o nome do filme')
diarias = int(input('Por quantos dias alugou o filme'))
tempo = int(input('Por quantos dias ficou com o filme'))

#Processamento
valor = tempo * 5
multa = 0

if tempo - diarias > 0:
    multa = 15

    total = valor + multa

#Saída
    print('Valor a ser pago', total)



