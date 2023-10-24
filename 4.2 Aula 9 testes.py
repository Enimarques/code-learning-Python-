frase = ('   Curso em video python  ')
print(len(frase)) #conta

print(len(frase.strip())) #conta sem os espaços inuteis

print(frase.replace('em', 'no')) #ele SÓ IMPRIME, MAS NÃO SALVA

print(frase)
frase = frase.replace('em', 'no') #AQUI SIM ELE SALVA A MUDANÇA

print(frase)

print('Curso' in frase)

print(frase.find('video'))  # ELE MOSTRA ONDE INICIA

'''SPLIT- CRIA UMA LISTA COM AS PALAVRAS'''
print(frase.split()) #print as palavras separadamente

dividido = frase.split()

print(dividido) # SERIA ['Curso', 'em', 'video']

print(dividido[1]) #RETORNARIA ''EM''.... a numeração entre colchetes

print(dividido[1][1]) #DENTRO de de 'em' me mostre a letra 1, que seria 'E'


