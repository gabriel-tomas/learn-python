list = ('ler', 'escrever', 'olhar', 'Jota')
for palavra in list:
    print(f'Na palavra \033[34m{palavra}\033[m tem:')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'\033[34m{letra}\033[m', end='')
        else:
            print(letra, end='')
    print('\n')
#for c in range(0, len(list)):
#    print(f'Na palavra \033[31m{list[c]}\033[m temos:')
#    for cont in range(0, len(list[c])):
#        if list[c][cont] in 'aeiou':
#            print(f'\033[31m{list[c][cont]}\033[m', end='')
#        else:
#            print(list[c][cont], end='')
#    print('\n')
