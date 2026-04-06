

dict_aluno1 = {'nome': 'Giovana', 'situacao': 'Matriculada', 'nota': 0 }
dict_aluno2 = {'nome': 'Gabriel Marques', 'situacao': 'Evadido', 'nota': 0 }
dict_aluno3 = {'nome': 'Mateus', 'situacao': 'Matriculada', 'nota': 0 }
dict_aluno4 = {'nome': 'Goão', 'situacao': 'Matriculada', 'nota': 0 }

lista_aluno = [dict_aluno1, dict_aluno2, dict_aluno3, dict_aluno4]

for aluno in lista_aluno:
    if aluno["situacao"] != 'Matriculada':
        continue
    nota = float (input(f'Digite a nota do aluno {aluno['nome']}:'))
    aluno['nota'] = nota 
    
print (lista_aluno)