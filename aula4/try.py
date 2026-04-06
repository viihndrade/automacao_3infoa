'''
Crie um script que solicita que o usuário digite dois números
inteiros. Após o programa deve realizar a divisão do primeiro número 
pelo segundo número. Por fim, deve mostrar o resultado 
da divisão.
'''
while True:
    try:
        n1 = int(input('Digite o primeiro número 1: '))
        n2 = int(input('Digite o segundo número 2: '))

        d = n1 / n2

        print ('O resultado é: ', d)
        break

    except ValueError:
        print('O valor digitado é inváldo, digite novamente.')
    except ZeroDivisionError:
        print('Não é possível dividir por 0. Tente novamente.')
    except Exception as bolinha:
        print('Ocorreu um erro', bolinha)