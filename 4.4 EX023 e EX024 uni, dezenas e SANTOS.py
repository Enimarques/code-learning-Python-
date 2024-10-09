n = input('Insira um numero entre 0 e 9999: ')
n = n.rjust(4 , '0') #4 seria a quantidade de caracteres que quero, e '0' seria o que quero colocar nos vazios a esquerda.

print(f'O seu número é {n.strip()}') #pra tirar os espaços a toa, caso ao inves de 0, colocasse ' '
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'centena: {n[1]}')
print(f'Milhares: {n[0]}')

'''Tambem teria a função n.zfill(4) que faria isso, só que nela nao especifico o que quero colocar nos espaços
Ela coloca zeros automaticamente'''


#INDICAR SE A CIDADE COMEÇA COM 'SANTOS'
cidade = (input('Qual o nome da sua cidade? ')).strip() #entre parenteses tira os espaços a toa
cidade = cidade.upper() #joga tudo pra maiusculo

print(f'Começa com a palavra SANTO: {'SANTO' in cidade[0:5]}')
print(cidade)


