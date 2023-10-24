#TIPOS PRIMITIVOS
# Como somar dois inputs sem apenas "juntar" eles.
n1 = input('Digite um numero:')
n2 = input('Digite um numero:')
s = n1 + n2
print('O valor vale', s)

#Pra resolver o problema de só juntar os numeros tenho que indicar que é um numero inteiro
#int (inteiro), float(flutuante, n° com ponto(virgula)), bool (True/False), string (tudo escrito entre aspas, textos)
#se eu não especifico o TIPO DA VARIAVEL, ela vem como STRING

n01 = int(input('Digite um numero:'))
n02 = int(input('Digite um numero:'))
t = n01 + n02

#tem uma forma nova de PRINTAR tbm. COLOCO COLCHETES, para 'puxar' a proxima variavel. E depois das aspas, coloco ".format(variavel)

#FORMA ANTIGA print('A soma entre', n01 , 'e', n02 , 'vale {}'.format(t))

print('A soma entre {} e {} vale {}'.format(n01 , n02 , t))

#Tenho uma opção de verificar o que uma variavel é:
    #coloco a sintaxe como abaixo, mas posso trocar o ".is..." por varias coisas: isalpha(letra), isnum(numero), isupper (MAIUSCULA)...

n = input('qualquer coisa')
print(n.isalnum())
