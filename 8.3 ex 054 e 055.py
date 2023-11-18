print('\033[46mExercicio numero 54 - datas de nascimento! \033[m')
maiores = 0
menores = 0
maior = 0
for c in range(1,7+1):
    idade = int(input(f'Digite a idade da {c}ª pessoa: '))
    if idade >= 21:
        maiores = maiores + 1
    else:
        menores = menores + 1

    if idade > maior:
        maior = idade
print(f"Ótimo, então nós temos aqui {maiores} pessoas com a idade igual ou maior que 21 anos e {menores} com menos de 21 anos. E a maior idade é {maior}.")

print('\n \033[41mExercicio de numero 55 - pesos\033[m')
maior_peso = 0
for p in range(1, 5+1):
    peso=float(input(f'Qual o peso da {p}ª pessoa: '))
    menor_peso = peso
    if peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso
print(f'O maior peso é o de {maior_peso}Kg, enquanto que o menor peso é o de {menor_peso}Kg.')