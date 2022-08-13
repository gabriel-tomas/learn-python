opc = 0
from time import sleep
n1 = int(input('Digite o 1 valor: '))
n2 = int(input('Digite o 2 valor: '))
while opc != 5:
    print('''[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos números
[5]Sair do programa''')
    opc = int(input('Digite uma opção: '))
    if opc == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif opc == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif opc == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n1 == n2:
            print('{} é igual a {}'.format(n1, n2))
        else:
            print('{} é maior que {}'.format(n2, n1))
    elif opc == 4:
        print('-=' * 12)
        print('Digite os novos valores: ')
        n1 = int(input('Digite o 1 novo valor: '))
        n2 = int(input('Digite o 2 novo valor: '))
    elif opc == 5:
        print('\033[31mPrograma Encerrado\033[m')
    else:
        print('\033[31mOPÇÃO INVALIDA!\033[m')
    sleep(1)
    print('-=' * 12)
