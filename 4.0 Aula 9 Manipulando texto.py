#Cadeia de texto = string
#String sempre fica entre '' ou ""

frase = 'Curso em vídeo Python'  #essa frase começa do 0 e até o 20. são 21 caracteres

#FATIAMENTO
frase[9] #pegou a 9a letra

frase[9:13] #essa seleciona do 9 ao 12, o 13 nao entra

frase[9:21:2] #seleciona do 9 ao 21 pulando de 2 em 2

frase[:5] #ele pega tudo ANTES DE 5

frase[15:] #seleciona até o final da frase

frase[9::3] # começa do 9 até o final, depois vai pulando de 3 em 3.

#ANALISE
len(frase) #seria lengh comprimento. 21 caracteres.

frase.count('o') #vai contar quantas vezes aparece o 'o'.

print(frase.find('deo')) #me mostra onde começa isso
'''Se ele nao encontrar algo, dar -1'''

'curso' in frase #retorna true or false

#ANALISE E FATIAMENTO
frase.count('o',0,13) #conta quantos o's começando do 0 ao 13

#TRANSFORMAÇÃO
frase.replace('Python','Android') #ele substitui um pelo outro

frase.upper() #coloca tudo que nao estava em maiusculo em maiusculo
frase.lower() #tudo minustuculo

frase.capitalize() #tudo pra minusculo e só deixa a 1a em maiuscula.

frase.title() #primeiras paalvras ficam em maiusculos

frase.strip() #REMOVE ESPAÇOS INUTEIS
frase.rstrip() #REMOVE SÓ OS DA DIREITA (os ultimos)
frase.lstrip() #remove só os da esquerda

#DIVISÃO
frase.split() #ele divide a frase nos espaços. As numerações ficam separadas, cada palavra vira uma linha na LISTA

#JUNÇÃO
'-'.join(frase) #junta as palavras com o traço no meio.

#Se quiser printar um texto todo
print("""Coloca tudo dentro de 3 aspas
      e ai ele printa tudo no final 
      junto, com as quebras de linha.""")