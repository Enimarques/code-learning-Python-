inicio = int(input("Digite o numero inicial: "))
final = int(input("Digite até qual numero quer contar: "))
passo = int(input('Digite de quantos em quantos vai contar: '))

for c in range(inicio, final+1, passo): #eu posso modificar as variaveis. Coloquei +1 por que quero que ele termine só no ultimo mesmo
    print(c)
print("Pronto, acabou")

print("#@#@"*20)
#Outro exemplo
s = 0 #somatorio recebe 0
for c in range(1,5):
    n = int(input('Dite um numero: '))
    s = s+n #s recebe o s + n que foi o valor digital

print(f'O somatório de todos os valores é igual a {s}')