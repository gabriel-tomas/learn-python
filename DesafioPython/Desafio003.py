n1 = int(input('\033[31mDigite um número:\033[m '))
n2 = int(input('\033[33mDigite outro número:\033[m '))
print('A soma para \033[32m{}\033[m e \033[32m{}\033[m é \033[4;32m{}\033[m!'.format(n1, n2, n1+n2))
