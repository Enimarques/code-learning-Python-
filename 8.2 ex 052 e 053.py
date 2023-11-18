print('\033[43mExercicio numero 52 - Número primo.\033[m')
n = int(input('Digite o número que deseja consultar: '))
#n = str(n) não posso usar esse, pq se não não uso operadores #Outra forma de se descobrir o ultimo digito é n%10. Sempre dará o último número.
if n in [2, 3, 5, 7] or (n > 1  and n%10 not in [0, 2, 5, 4, 6, 8] and n%3 != 0 and n%7 != 0):
    print(f'{n} é um número primo!')
else:
    print(f'{n} não é um número primo.')

print('\033[42mExercicio numero 53 - É um palídramo? \033[m')
frase = input('Digite a frase para verificarmos se é ou não um palídromo: ').strip()
frase = frase.lower().replace(" ", "")
frase_invertida = frase[::-1]
if  frase == frase_invertida:
    print(f"Sim, essa frase: '{frase}' é um palídramo, ou seja é igual a frase '{frase_invertida}.")
else:
    print(f"Não, a frase: '{frase}' não é um palídramo.")