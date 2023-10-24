#ex 16
import math #eu posso importar só uma função, sendo assim não preciso usar o math.função- só coloco a função(o que quero)
n = float(input('Digite um numero que deseja ver arrendodado '))

print(f'O número {n} na sua forma inteira é {math.trunc(n)}')


#exercicio 17
oposto = float(input('Qual é o valor do cateto oposto? '))
adjascente = float(input('Qual o valor do cateto adjascente? '))
hip = math.hypot(oposto , adjascente) #é a formula da hipotenusa
hip2 = math.sqrt((oposto**2+adjascente**2)) #é a hipotenusa crua
print(f'{hip:.2f} que é igual a {hip2}')

from math import radians,sin,cos,tan
#exercicio 18
a1 = float(input('Digite o primeiro angulo: '))
radiano = radians(a1) #O python precisa do angulo em radiano.
sen = sin(radiano)
cos = cos(radiano)
tan = tan(radiano)
print('O valor do seno é {:.2f}, do cosseno é {:.2f} e da tangente é {:.2f}'.format(sen, cos, tan))
