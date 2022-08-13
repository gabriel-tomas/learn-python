c1 = int(input('\033[34mPrimeiro comprimento: '))
c2 = int(input('Segundo comprimento: '))
c3 = int(input('Terceiro comprimento: \033[m'))
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('\033[32;7mÉ possível\033[m')
    if c1 == c2 == c3:
        print('Equilatero')
    elif c1 == c2 or c2 == c3 or c1 == c3:
        print('Isósceles')
    elif c1 != c2 != c3:
        print('Escaleno')
else:
    print('\033[31;7mNão é possível\033[m')
