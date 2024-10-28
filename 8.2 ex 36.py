nome = input('Olá, bem vindo a Enimarques Imovéis. Qual o seu nome?')
print(f'Certo {nome}, vamos verificar se você pode comprar esse imóvel.')
imovel = int(input('Qual o valor do imóvel que você quer comprar?'))
salario = float(input('Quanto você recebe por mês de salário?'))
tempo = int(input('Em quantos anos você quer financiar esse imóvel?'))

tempo = tempo*12
prestacao = imovel/tempo
margem = salario*0.3

if prestacao > margem:
  print(f'Me desculpe {nome}, mas o valor da prestação, R${prestacao:.2f} excedeu sua margem consignável que era de R${margem:.2f}')
else:
  print(f'Parabéns {nome}, vamos aceitar seu financiamento. \n Seu imóvel será financiado em {tempo} parcelas no valor de R${prestacao:.2f}.')