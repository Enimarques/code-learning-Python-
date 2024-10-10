'''from random import choice,choices
p1=input('Qual nome do aluno 1?')
p2=input('Qual nome do aluno 2?')
p3=input('Qual nome do aluno 3?')
p4=input('Qual nome do aluno 4?')

alunos=[p1,p2,p3,p4]

escolhido=choices(alunos,k=2)
print(f'Os alunos escolhidos são {' e '.join(escolhido)}')'''


import random
pc_n = random.randint(0,5)
n = int(input("Tente adivinhar o número que o computador pensou, de 0 a 5. Qual foi?"))

if pc_n == n:
  print('Parabéns, você acertou!')
else:
  print('Poxa, não foi dessa vez.')

print(f'O número escolhido pelo pc foi: {pc_n}')