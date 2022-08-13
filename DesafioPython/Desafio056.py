media = 0
maiorhomem = 0
nomehomemvelho = ''
contamul = 0
for c in range(1, 5):
    nome = str(input('Nome da {} pessoa: '.format(c)))
    idade = int(input('Idade da {} pessoa: '.format(c)))
    sexo = str(input('Sexo da {} pessoa(M/F): '.format(c))).upper()
    media = media + idade
    if c == 1 and sexo == 'M':
        maiorhomem = idade
        nomehomemvelho = nome
    if sexo == 'M' and idade > maiorhomem:
        maiorhomem = idade
        nomehomemvelho = nome
    if idade < 20 and sexo == 'F':
        contamul = contamul + 1
print('A média de idade do grupo é {}'.format(media/4))
print('O homem mais velho é o {} com {} anos de idade'.format(nomehomemvelho, maiorhomem))
print('Tem {} mulheres com menos de 20 anos de idade'.format(contamul))
