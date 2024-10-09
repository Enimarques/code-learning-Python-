from random import choice,choices
p1=input('Qual nome do aluno 1?')
p2=input('Qual nome do aluno 2?')
p3=input('Qual nome do aluno 3?')
p4=input('Qual nome do aluno 4?')

alunos=[p1,p2,p3,p4]

escolhido=choices(alunos,k=2)
print(f'Os alunos escolhidos são {' e '.join(escolhido)}')
