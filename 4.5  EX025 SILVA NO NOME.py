nome = input('Qual o seu nome completo? ')

#print(f'Seu nome tem SILVA: {nome.find('SILVA')}')
print(f'Seu nome tem SILVA: {'SILVA' in nome.upper().split()}')  # ja posso jogar o upper direto aqui, e não altera o nome, só pra condição apresentada!
#o .split é pra caso de ter nome como SILVANEI

print(nome)
