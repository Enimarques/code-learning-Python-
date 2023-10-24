n = int(input('Digite um valor para descobrir se é PAR ou IMPAR: '))
resto = n % 2

if resto == 0:
    print(f'O número {n} é PAR.')

else:
    print(F'O número {n} é ÍMPAR. ')


#ex031 paasagens
p = (float(input('Qual a distãncia da sua viagem? ')))

if p<=200:
    print(f'A sua passagem custará R${p*0.5:.2f}')

else:
    print(f'A sua passagem custará R${p*0.45:.2f}')