frase = input('Digite uma frase: ').strip()
frase = frase.upper()
frase = frase.replace('Ã', 'A')
frase = frase.replace('Á', 'A')
frase = frase.replace('À', 'A')

A = frase.count('A')
p_a = frase.find('A') #quandoa aparece a primeira (esquerda)
u_a = frase.rfind('A') #quando aparece a ultima (direita) right

print(f"Sua frase tem {A} letras a's")
print(f"A primeira letra 'a' aparece na posição {p_a + 1}.")
print(f"A ultima letra 'a' aparece na posição {u_a + 1}.")

print(frase)


#LISTA
nome = input('Digite seu nome completo: ')
nome = nome.split()

print(f'Primeiro nome = {nome[0]}. \n'
      f'Ultimo nome = {nome[-1]}') #quando venho de tras pra frente vale tbm, -2 penultimo, -3 antepenultimo

