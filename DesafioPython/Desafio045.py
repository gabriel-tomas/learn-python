from random import choice
from time import sleep
ecp = choice(['pedra', 'papel', 'tesoura'])
eus = str(input('Pedra, papel? ou tesoura? ')).lower().strip()
print('\033[33mJo', end='')
sleep(1)
print('\033[31mken', end='')
sleep(1)
print('\033[35mpo\033[m\n')
if ecp == eus:
    print('Empate, o Computador escolheu {} e você {}'.format(ecp.title(), eus.title()))
elif ecp == 'pedra' and eus == 'papel':
    print('\033[32mVENCEU!!!\033[m\n{} vence {}'.format(eus.title(), ecp.title()))
elif ecp == 'pedra' and eus == 'tesoura':
    print('\033[31mPERDEU\033[m\n{} perde para {}'.format(eus.title(), ecp.title()))
elif ecp == 'papel' and eus == 'pedra':
    print('\033[31mPERDEU\033[m\n{} perde para {}'.format(eus.title(), ecp.title()))
elif ecp == 'papel' and eus == 'tesoura':
    print('\033[32mVENCEU!!!\033[m\n{} vence {}'.format(eus.title(), ecp.title()))
elif ecp == 'tesoura' and eus == 'pedra':
    print('\033[32mVENCEU!!!\033[m\n{} vence {}'.format(eus.title(), ecp.title()))
elif ecp == 'tesoura' and eus == 'papel':
    print('\033[31mPERDEU\033[m\n{} perde para {}'.format(eus.title(), ecp.title()))
else:
    print('Rode novamente e digite uma das palavras do Jokenpo')
