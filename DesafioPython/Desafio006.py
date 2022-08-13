n = float(input('\033[35mDigite um número: '))
print('O dobro é \033[4m{}\033[m\n\033[35mO triplo é \033[4m{}\033[m\n'
      '\033[35mA raiz quadrada é \033[1;30;42m{:.2f}\033[m'.format((n*2), (n*3), pow(n, (1/2))))
