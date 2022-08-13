import random
import time
print('\033[32m_-' * 17, 'Pensando num número entre 0 e 5...', '_-' * 17, '\033[m\033[33m')
time.sleep(3)
n = random.randint(0, 5)
espaco = ' '*30
graca = '_'*45
print('{}{}'.format(espaco, graca))
r = input('{}\033[35mTente adivinhar qual foi o número escolhido: \033[m'.format(espaco))
if int(r) == n:
    print('{}              \033[1;32mVOCÊ VENCEU!!'.format(espaco))
if int(r) != n:
    print('{}        \033[31;1mVocê perdeu, o numero era \033[4m{}'.format(espaco, n))
