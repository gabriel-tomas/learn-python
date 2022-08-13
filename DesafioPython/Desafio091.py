from random import randint
from operator import itemgetter
from time import sleep
dicionario = {}
print('Valores tirados:')
for jogadores in range(1, 5):
    dado = randint(1, 6)
    print(f'    O jogador {jogadores} tirou = {dado}')
    dicionario[f'jogador {jogadores}'] = dado
    sleep(1)
print(dicionario)
list_sorted = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
print(list_sorted)
print('Ranking:')
for i, jogad in enumerate(list_sorted):
    print(f"    {i + 1}- {jogad[0]} com {jogad[1]}")
    sleep(1)
