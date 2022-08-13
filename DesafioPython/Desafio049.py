n = int(input('Diga um número: '))
print('\033[1;35m=\033[m'*12)
for c in range(0, 11):
      print('\033[32m{}x{}= {}'.format(n, c, n * c))
print('\033[1;35m='*12)
