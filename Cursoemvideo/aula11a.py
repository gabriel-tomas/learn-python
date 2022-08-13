frase = 'Olá, Mundo!'
print('\033[1;33;40m{}\033[m'.format(frase[0:4]), end='')
print('\033[1;31;40m{}\033[m'.format(frase[4:]))

