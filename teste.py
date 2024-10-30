'''from random import choice,choices
p1=input('Qual nome do aluno 1?')
p2=input('Qual nome do aluno 2?')
p3=input('Qual nome do aluno 3?')
p4=input('Qual nome do aluno 4?')

alunos=[p1,p2,p3,p4]

escolhido=choices(alunos,k=2)
print(f'Os alunos escolhidos são {' e '.join(escolhido)}')


import random
pc_n = random.randint(0,5)
n = int(input("Tente adivinhar o número que o computador pensou, de 0 a 5. Qual foi?"))

if pc_n == n:
  print('Parabéns, você acertou!')
else:
  print('Poxa, não foi dessa vez.')

print(f'O número escolhido pelo pc foi: {pc_n}')'''

'''print('Desafio do jogo melhorado e resumido')
import random
n = 1 #contador
pc = random.randint(0,10)
eu = int(input('Okay, vamos brincar um pouco, pensei em um numero de 0 a 10, tente adivinhar qual é: '))
if pc == eu:
  print(f'Parábens miseravão, acertou de primera, após {n} tentativa.')
else:
  while pc != eu:
    eu = int(input('Errou vacilão, tenta de novo trouxa: '))
    n = n+1
  print(f'Ai sim, até que enfim em? Você precisou de {n} tentativas para acertar o número.')'''
    
print('Fatorial agora com função "for"')
n = int(input('Qual numero inteiro voce quer ver o fatorial?'))  
fatorial = 1
for c in range (n,0,-1):
  fatorial = fatorial * c
  print(fatorial)
print(f'O fatorial de {n} é igual a {fatorial}') 