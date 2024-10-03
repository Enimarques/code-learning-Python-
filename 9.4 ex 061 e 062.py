print("\033[44mPA com while\033[m")
n1 = int(input("Qual o primeiro termo da sua PA?"))
r = int(input("Qual a razão da sua PA?"))
cont = 1
termos = int(input("Quantos termos da sua PA você quer descobrir?"))
while cont<=termos:
    print(f"O {cont}ª termo da sua PA é {n1}")
    cont += 1
    n1 = n1+r

from time import sleep
sleep(2)

print("\033[42mQuantos termos a mais voce quer ver\033[m")
n1 = int(input("Qual o primeiro termo da sua PA?"))
r = int(input("Qual a razão?"))
cont =1
termos = int(input("Quantos termos da sua PA você quer descobrir?"))
while cont<=termos:
    print(f'O {cont}º termo da sua PA é {n1}.')
    cont = cont +1
    n1 = n1 + r
mais = int(input("Quantos termos a mais você quer ver na sua PA?"))
if mais == 0:
    print("Okay, muito obrigado.Terminamos por aqui!")

while mais != 0:
    repetições = mais
    while repetições != 0:
        n1 = n1 + r
        print(f'O {cont}º termo da sua PA é {n1}.')
        repetições = repetições - 1
        cont = cont + 1
    mais = int(input("Quantos termos a mais você quer ver?"))
    if mais == 0:
        print("Okay, muito obrigado.Terminamos por aqui!")

