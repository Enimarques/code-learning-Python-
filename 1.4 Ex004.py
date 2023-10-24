#Testando a utilização dos isSOMETHING
nome = input('Qual o seu nome?')
print('Esse input é número? {}'.format(nome.isnumeric()))
print('Esse input é numero e/ou letra? {}'.format(nome.isalnum()))
print('Esse input é em maiusculo? {}'.format(nome.isupper()))
print('Esse input é minusculo? {}'.format(nome.islower()))
print('Esse input é só letra? {}'.format(nome.isalpha()))
print('Esse input só tem espaços? {}'.format(nome.isspace()))
print('Esse input é imprimível? {}'.format(nome.isprintable()))
# print(f'Qual o tipo primitivo desse input? {}'.format(type(nome))) UM JEITO DE FAZER
print(f'Qual o tipo primitivo desse input? {type(nome)}')


# Capitalizada é se tem maiuscula e minuscula. .istitle.

