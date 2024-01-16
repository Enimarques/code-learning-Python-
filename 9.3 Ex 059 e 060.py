print('\033[1:43mExercicio 059- 2 valores e opções\033[m')
n1=int(input('Digite o primeiro valor que você deseja tratar: '))
n2=int(input('Digite o segundo valor que você deseja tratar: '))
print('\033[7:31mMuito bem, agora escolha umas das opções abaixo, e indique o que deseja fazer.\033[m ')
o = 0
while o != 5:
    o = int(input('[1] Somar\n'
                  '[2] Multiplicar\n'
                  '[3] Maior\n'
                  '[4] Novos números\n'
                  '[5] Sair do programa.\n'
                  'O que você deseja fazer?'))
    if o == 1:
        print(f'\033[7:33mA soma de {n1} e {n2} é {n1+n2}\033[m.')
    elif o == 2:
        print(f'\033[7:33mA multiplicação de {n1} e {n2} é {n1*n2}\033[m.')
    elif o ==3:
        if n1>n2:
            print(f'\033[7:33mO maior dos dois valores é o número: {n1}\033[m.')
        elif n2>n1:
            print(f'\033[7:33mO maior dos dois valores é o número: {n2}\033[m.')
        else:
            print(f'\033[7:33mOs dois números são iguais: {n1}\033[m.')
    elif o == 4:
        n1 = int(input('Digite o novamente primeiro valor que você deseja tratar: '))
        n2 = int(input('Digite agora o segundo valor que você deseja tratar: '))
print('Muito obrigado, espero que tenha encontrado o que queria. ')
from time import sleep
sleep(0)

print('\n'
      '\033[4:44O fatorial de um número!\033[m')
n=int(input(f'Qual o número você quer ver o fatorial?'))
i = 1
fatorial = 1
while i<=n:
    fatorial = fatorial * i
    i = i + 1

print(f'O fatorial de {n} é {fatorial}!')