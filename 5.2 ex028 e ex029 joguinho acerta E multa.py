import random
pc_n = random.randint(0,10)

n = int(input('Advinhe o número que o computador pensou: '))
if pc_n == n:
    print(f'Parabéns, você acertou, é o cara mesmo ohr!')

else:
    print(f'Ihhh, mais sorte na próxima, LOSER')

print(pc_n)




#029
v = int(input('Com qual velocidade você passou? KM/h '))

if v>80:
    print(f'Você foi multado. Sua velocidade foi de {v} Km/h \n'
          f'Logo, vai pagar uma multa no valor de R${(v-80)*7},00 para aprender.')
else:
    print('Dessa vez você escapou.')