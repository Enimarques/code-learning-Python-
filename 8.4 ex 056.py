print("\033[41mExercicio de numero 56 - dados de pessoas\033[m")
media = 0
velho = 0
mais_velho = 0
jovens = 0
for c in range(1, 4+1):
    nome1 = input(f'Qual o nome da {c}ª pessoa? ').strip().capitalize()
    idade1 = int(input(f'Qual a idade da {c}ª pessoa? '))
    sexo1 = input(f'Qual o sexo da {c}ª pessoa? \033[33m(Digite M para masculino e F para feminimo.)\033[m').strip().upper()
    media = media + idade1

    if idade1 > velho and sexo1 == 'M':
        velho = idade1
        mais_velho = nome1

    if idade1 < 20 and sexo1 == 'F':
        jovens = jovens + 1


print(f'A média de idade dessas pessoas é igual a: {media/4}')
print(f'O nome do homem mais velho é: {mais_velho}')
print(f'{jovens} mulher(es) tem menos do que 20 anos.')