n = int(input('Diga um número: '))
print('\033[1;35m=\033[m'*12)
print('{}x1={}'.format(n, n*1), '\n\033[45m{}x2={}\033[m'.format(n, (n*2)),
      '\n\033[1;45m{}x3={}\033[m'.format(n, (n*3)),
      '\n\033[1;45m{}x4={}\033[m'.format(n, (n*4)),
      '\n\033[1;45m{}x5={}\033[m'.format(n, n*5),
      '\n\033[1;45m{}x6={}\033[m'.format(n, (n*6)),
      '\n\033[1;45m{}x7={}\033[m'.format(n, (n*7)),
      '\n\033[1;45m{}x8={}\033[m'.format(n, (n*8)),
      '\n\033[1;45m{}x9={}\033[m'.format(n, (n*9)),
      '\n\033[1;45m{}x10={}\033[m'.format(n, (n*10)))
print('\033[1;35m='*12)
