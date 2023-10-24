# OPERADORES ARITMÉTICOS
# Para eu usar O SIMBOLO DE IGUALDADE eu uso 2 IGUAIS (==), por que só 1 = é 'RECEBE'
# % == não é de porcentagem na programação, ele é O "Resto da divisão"
# // == SIMBOLO PARA DIVISÃO INTEIRA. Seria a divisão sem virgulas e com resto da divisão.
# **(1/2) == RAIZ QUADRADA (potencia de meio é a raiz quadrada)
# != QUER DIZER 'DIFERENTE' NÃO IGUAL

# eu consigo brincar de multiplicar nomes ou sinais. Além disso eu posso especificar os espaços de uma respota como abaixo:
nome = input('Qual é o seu nome?')
print('Prazer em te conhecer {:20}!'.format(nome))

# esse {:20} indica a quantidade de caracteres que eu quero que mostre.
# posso ainda colocar outras coisas como alinhado (<,>,^) ou ainda arrodeado por =({:20=^})

print('Testando se mudou algo {:=^20}!'.format(nome))

print('E agora {:*^30}!'.format(nome))

# QUEBRA DE LINHA == /n
# PARA NÃO QUEBRAR == , end=''
