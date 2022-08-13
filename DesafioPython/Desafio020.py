a1 = input('\033[34mPrimeiro aluno: ')
a2 = input('\033[31mSegundo aluno: ')
a3 = input('\033[33mTerceiro aluno: ')
a4 = input('\033[32mQuarto aluno: ')
from random import shuffle
lista = [a1, a2, a3, a4]
shuffle(lista)
a = ' '.join(lista)
b = a.split()
print('\033[34m{} \033[31m{} \033[33m{} \033[32m{}'.format(b[0], b[1], b[2], b[3]))
