from random import randint
cpu = randint(0, 10)
print('Adivinhe o número da CPU de 0 a 10')
jogador = int(input('Digite seu valor: '))
tentativas = 0
while cpu != jogador:
    jogador = int(input('Digite novamente até acertar: '))
    if jogador > cpu:
        print('Mais para baixo!')
    if jogador < cpu:
        print('Mais para cima!')
    tentativas = tentativas + 1
print('\nForam no total {} tentativas para chegar até a resposta correta!'.format(tentativas+1))
