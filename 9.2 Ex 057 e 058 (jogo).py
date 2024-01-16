#minuto 28:15
import time
from time import sleep
print("\033[45m EXERCICIO 057- PROGRAMA QUE LER SEXO\033[m")
s = ''
while s != "M" and s != "F":
    s = input("Qual o seu Sexo? M/F ").upper()
    if s == "M":
        print("Então voce é homem!")
    if s == "F":
        print("Então voce é mulher!")
print("fim")
sleep(0)

print("\033[46m Refazendo o desafio 28 de advinhação\033[m")
import random
pc = random.randint(1,10)
nome = input("Olá, qual o seu nome? ")
r = '' #r tem que ter sido definido
while r != "S" and r != 'N': #quero que repita a pergunta se a resposta for errada. Se não for segue pro jogo ou pro fim!
    r = input(f"Tudo bem {nome}? Vamos jogar? S/N " ).upper()
    if r!='S' and r!='N':
        print("Sua resposta foi incoreta. Tente de novo, lembre-se, use 'S' para Sim e 'N' para Não. ")
    else:
        if r == 'S':
            print("Okay, então vamos começar!")
            c = 1 #contador
            n = int(input(f"Tente adivinhar qual número eu escolhi {nome}, de 1 a 10, vamos ver se você é bom mesmo: "))
            if n == pc:
                print(f'Parabens {nome}, você acertou na primeira tentantiva! É o bixão mesmo!')
            else:
                while n != pc:
                    n = int(input(f'É {nome}, infelizmente não foi dessa vez. TENTE DE NOVO:'))
                    c = c + 1
                if c>5:
                    print(f'Até que enfim {nome}, você acertou depois de {c} tentativas.')
                else:
                    print(f'Acertou, Parabéns. Você precisou apenas de {c} tentativas.')

        elif r == 'N':
            print("Okay, que pena, então até a próxima!")

print(f"Até mais {nome}.")


