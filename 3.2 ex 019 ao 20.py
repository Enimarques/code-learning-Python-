#sortear aluno 019
aluno1 = input('Escreva o nome do aluno 01: ')
aluno2 = input('Escreva o nome do aluno 02: ')
aluno3 = input('Escreva o nome do aluno 03: ')
aluno4 = input('Escreva o nome do aluno 04: ')

alunos = [aluno4, aluno3, aluno2, aluno1] #colocou colchetes cria uma LISTA

import random
sorteado = random.choice(alunos) #choice sozinho seleciona um

print(f'O aluno sorteado para limpar o quadro é o(a) {sorteado}')

#ESCOLHE DOIS DOS 4 PARA FAZER ATIVIDADE
atividade = random.choices(alunos, k=2) #Choices com s vai me dizer quantos escolhidos

print(f'Depois disso os que farão a atividade serão o {" e o ".join(atividade)}!')
#primeiro "" coloco o que separa as variaveis, enquanto que o .join(variavel) vai juntar elas

'''randrange(start, stop, step): Essa função gera um número inteiro aleatório entre start (inclusive) e stop (exclusivo),
# com um intervalo de step. Por exemplo, random.randrange(1, 10, 2) pode retornar valores como 1, 3, 5, 7, ou 9.'''

#ESCOLHE A ORDEM PARA APRESENTAR O TRABALHO
apresentacao = random.sample(alunos, k=4) #nesse eu consigo limitar a quantidade de selecionados, independete do tamanho da lista
print(f'A ordem a ser apresentado será: {" , ".join(apresentacao)}')

#Poderia ser tambem assim:
random.shuffle(alunos)
print(f'A ordem de apresentação será:  \n {alunos}')