n = int(input('\033[34mDigite um número: \033[m'))
if (n % 2) == 0:
    print('\033[32;7;1mpar\033[m')
else:
    print('\033[33;7;1mimpar\033[m')
