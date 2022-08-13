from time import sleep
p = str(input('Iniciar contagem para os fogos? ')).lower().strip()
if p == 'sim':
    for c in range(10, -1, -1):
        sleep(1)
        print(c)
        if c == 0:
            print('\033[33mBOOMM!!')
if p == 'não':
    print('\033[31mInicie o programa novamente caso queira iniciar a contagem.\033[m')
