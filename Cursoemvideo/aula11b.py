n = str(input('Números: '))
a = n.split(',')
print('Os valores são \033[33m{}\033[m e \033[31m{}\033[m!!!'.format(a[0], a[1]))
