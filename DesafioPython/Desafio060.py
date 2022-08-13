"""n = int(input('Factorial: '))
n1 = n
a = n
r = a
while a != 0:
    print(n1, end='')
    print('x' if n1 > 1 else '=', end='')
    n1 = n1 - 1
    if n1 != 0:
        r = r * n1
    a = a - 1
print('{}'.format(r))"""

n = int(input('Digite um numero para o factorial: '))
f = 1
for c in range(n, 0, -1):
    print(c, end='')
    if c > 1:
        print('x', end='')
    else:
        print('=', end='')
    f = f * c
print(f)
