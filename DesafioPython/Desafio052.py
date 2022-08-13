ni = int(input('Digite um número inteiro: '))
o = 0
for c in range(1, ni+1):
    if ni % c == 0:
        print('\033[32m{}'.format(c), end=' ')
        o = o + 1
    else:
        print('\033[31m{}'.format(c), end=' ')
if o == 2:
    print('\n\033[m{} é primo pois ele foi dividido por um e por ele mesmo'.format(ni))
elif o > 2:
    print('\n\033[m{} não é primo pois ele é divisivel por mais de dois'.format(ni))
else:
    print('\n\033[m{} não é primo'.format(ni))
