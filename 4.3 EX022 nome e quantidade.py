nome = input('Informe seu nome por completo: ').strip() #ja pra eliminar espaços atoa
up = nome.upper()
low = nome.lower()
num = nome.replace(" ",'')
pnome = nome.split() #antes de fazer a contagem preciso fazer nome.split separado
'''Ou poderia colocar assim
1. pnome = len(nome.split()[0]) que contaria o primeiro nome
print(pnome)
2. print(len(pnome[0]))

'''

print(up)
print(low)
print(f'{len(num)} é a quantidade de caracteres de "{num}", sem espaços')
print(f'{len(nome) - nome.count(' ')} é a quantidade de caracteres que "{nome}", sem espaços tem.')#aqui contei quantos espaços e subtrai

print(f'{len(nome)} é a quantidade de caracteres de "{nome}", com espaços')

print(f'{len(pnome[0])} é a quantidade de caracteres do primeiro nome: {pnome[0]}')

