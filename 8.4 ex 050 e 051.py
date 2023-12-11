print(f'\033[45mExercicio número 50 - Soma dos números pares!\033[m')
total = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}° número: '))
    if n%2 == 0:
         total = total + n

print(f'A soma total de todos os números é {total}.')

import time
time.sleep(3)

print('\n\033[47mExercicio número 51 - Progressão aritmética!\033[m')
n1 = int(input("Qual o primeiro termo da sua PA? "))
r = int(input('Qual a razão da sua PA? '))
for c in range(1, 11):
    print(f'O {c}° termo da sua PA é {n1}.')
    n1 = n1 + r
print(f'Pronto, esses foram os {c} termos da sua PA.')
