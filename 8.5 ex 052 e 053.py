print('\033[43mExercicio numero 52 - Número primo.\033[m')
n = int(input('Digite o número que deseja consultar: '))
#n = str(n) não posso usar esse, pq se não não uso operadores #Outra forma de se descobrir o ultimo digito é n%10. Sempre dará o último número.
if n in [2, 3, 5, 7] or (n > 1  and n%10 not in [0, 2, 5, 4, 6, 8] and n%3 != 0 and n%7 != 0):
    print(f'{n} é um número primo!')
else:
    print(f'{n} não é um número primo.')

#outra forma de fazer
num = int(input("\nDigite um numero que queira consultar se é primo ou não: "))
total = 0 #total de vezes que ele fo divisivel
for c in range(1, num+1):
    if num%c == 0: #se o numero for divisivel pelos anteriores a ele e resto = a 0
        print("\033[31m", end='')
        total = total + 1 #toda vez que ele passar por um c que é divisivel ele vai somar
    else:
        print("\033[35m", end='')
    print(f'{c}', end=' ')
print(f"\n\033[mO número {num} foi divisível no total de {total} vezes.")
if total == 2:
    print(f"O número {num} é primo")
else:
    print(f'O numero {num} não é primo!')


print('\n\n\033[42mExercicio numero 53 - É um palídramo? \033[m')
frase = input('Digite a frase para verificarmos se é ou não um palídromo: ').strip()
frase = frase.upper().replace(" ", "")
frase_invertida = frase[::-1]
if  frase == frase_invertida:
    print(f"Sim, essa frase: '{frase}' é um palídramo, ou seja é igual a frase '{frase_invertida}'.")
else:
    print(f"Não, a frase: '{frase}' não é um palídramo.")