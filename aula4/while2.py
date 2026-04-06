#Estrutura de Repetição: while

while True:
    usuario = input('Digite seu login: ')
    senha = input('Digite sua senha: ')

    if (usuario== 'admin' and senha == '123') :
        break
    else:
        print('Falha ao ralizar o login.')

print ('Bem vindo ao sistema!')