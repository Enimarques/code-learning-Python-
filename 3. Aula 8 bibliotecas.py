#UTILIZANDO MÓDULOS- BIBLIOTECAS
#Para ter algumas funcionalidades a mais eu preciso importar bibliotecas para aumentar funções
#Pra isso, preciso dar comando IMPORT
#import -alguma biblioteca- ele importa tudo. Para importar só alguma coisa especifica dentro da biblioteca eu coloco 'from-biblioteca-import'


import math
from math import sqrt, floor, ceil #posso importar dessa forma tambem

#ceil- arredonda pra cima, floor- arredonda pra baixo, sqrt - raiz quadrada, pow - potencia

num = int(input('Digite um número: '))
raiz = math.sqrt(num) #poderia jogar o math.ceil aqui tbm direto
#raiz = math.ceil(math.sqrt(num))

print(f'A raiz de {num} é {math.ceil(raiz)}') #essa é a maneira 01 de fazer
print('A raiz de {} é {} !'.format(num, math.floor(raiz))) #forma 02 de fazer, só que pedi pra baixo agora

# import random (serve para randomizar um numero)
import random
n1 = random.random() #ele da um numero de 0 a 1
print(f'{n1}')

n2 = random.randint(1,100) #da um numero inteiro, no intervalo de 1 a 100 que coloquei)

print(n2)

import emoji #biblioteca de emojis
emoji_bloquado = emoji.emojize("🌎")
print(f"Isso é tudo pessoal {emoji_bloquado}")




