from random import randint
from time import sleep
lista_jogos = []
jogos = []
print(f'{"=-" * 25}\n{"JOGOS MEGA SENA":^50}\n{"-=" * 25}\n')
num_jogos = int(input('Quantos jogos? '))
print(f'{"=" * 10}Sorteando {num_jogos} jogos{"=" * 10}')
for nums_jogos in range(0, num_jogos):
    while True:
        nums_lista = randint(1, 60)
        if nums_lista not in jogos:
            jogos.append(nums_lista)
        if len(jogos) == 6:
            break
    lista_jogos.append(jogos[:])
    jogos.clear()
for indice, jogos_list in enumerate(lista_jogos):
    jogos_list.sort()
    print(f'\033[36m{indice + 1}ª Jogo {jogos_list}')
    sleep(1)
print(f'\033[m{"=" * 17}Fim{"=" * 17}')
