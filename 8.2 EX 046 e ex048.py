print('\033[46mExercicio 46 - Fogos de artificios contagem regressiva\033[m')
import time
print("Okay, então vamos lá comemorar a virada de ano!")
for c in range(5, 0, -1):
    print(c)
    time.sleep(1)
print("\033[43mFeliz 2024!\033[m\n")
time.sleep(2)

print('\033[45mExercicio 47- Numeros pares de 1 a 50\033[m\n')
for c in range(2,51,2):
    print(c, end=' ') #para não ter fim, continuar contando no lado

print("\n\n\033[44mExercicio 48- Soma de de numeros impares multiplos de 3 \033[m")
time.sleep(4)
soma = 0 #tenho que ter um acumulador para conseguir essa soma
cont = 0 #esse é meu contador, quero que ele me diga quantos numeros foram.
for c in range(1,500+1,2):
    if c%3 == 0:
        soma = soma + c #posso escrever isso assim soma += c
        cont += 1 # ou cont = cont + 1
print(f'A soma dos {cont} valores será {soma}.')
