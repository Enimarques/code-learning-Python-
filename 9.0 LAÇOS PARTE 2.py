"""A estrutura com FOR só serve se eu saber o limite final, se não souber ela não serve"""
#Precisaria de uma CONDIÇÃO
"""Vou repetir ENQUANTO não se cumprir algo. ESTRUTURA DE REPETIÇÃO COM TESTE LÓGICO
enquanto não
    passo
pega"""

'''while not apple
    passo
pega'''

print('Vamos lá descobrir qual seu sexo?')
sexo = input('Qual o seu sexo? Digite M para Masculino ou F para feminino: ').upper()
if sexo != 'M' and sexo != 'F':
    while sexo != 'M' and sexo != 'F':
        sexo = input('Opção errada, digite M para homem e F para mulher: ').upper()
if sexo == 'M':
    print('Certo, então você é homem!')
    
if sexo == 'F':
    print('Okay senhora, voce é uma mulher.')

