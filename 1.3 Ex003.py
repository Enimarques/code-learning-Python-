n1 = int(input('Qual é o primeiro numero da soma?'))
n2 = int(input('Qual é o segundo?'))
s = n1 + n2

print('O valor da soma entre {} e {} é {}'.format(n1, n2, s))

# outra maneira de fazer é utilizando o fstring
print(f'A soma entre {n1} e {n2} é {s}, ou é igual a {n1 + n2}!')

