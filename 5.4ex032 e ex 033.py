ano = int(input('Qual ano voce quer saber? '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano de {ano} é bissexto! ')

else:
    print(f'O ano de {ano} não é bissexto!')


#ex34
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número: '))

maior = 0
menor = 0

if n1>=n2 and n1>=n3:
    maior = n1
if n1<=n2 and n1<=n3:
  menor = n1
if n2>=n1 and n2>=n3:
    maior = n2
if n2<=n1 and n2<=n3:
    menor = n2
if n3>=n1 and n3>=n2:
    maior = n3
if n3<=n1 and n3<=n2:
    menor = n3
    
print(f'O maior número é o {maior}, enquanto que o menor é {menor}')

'''Ou'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

# Inicializando com os primeiros valores para maior e menor
maior = n1
menor = n1

# Verificando o maior número
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

# Verificando o menor número
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print(f'O maior número é o {maior}, enquanto que o menor é {menor}')
