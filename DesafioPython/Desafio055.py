peso1 = 0
for c in range(0, 6):
    peso = float(input('Digite o peso: '))
    peso1 = peso, peso1
a = str(peso1).split('(')
b = ','.join(a)
c = b.replace(')', '')
d = c.replace(' ', '')
e = d.replace(',', ' ')
f = e.split()
d = float(f[0]), float(f[1]), float(f[2]), float(f[3]), float(f[4]), float(f[5])
if d[0] > d[1] and d[0] >  d[2] and d[0] > d[3] and d[0] > d[4] and d[0] > d[5]:
    print('{} é o maior'.format(d[0]))
elif d[1] > d[0] and d[1] > d[2] and d[1] > d[3] and d[1] > d[4] and d[1] > d[5]:
    print('{} é o maior'.format(d[1]))
elif d[2] > d[0] and d[2] > d[1] and d[2] > d[3] and d[2] > d[4] and d[2] > d[5]:
    print('{} é o maior'.format(d[2]))
elif d[3] > d[0] and d[3] > d[1] and d[3] > d[2] and d[3] > d[4] and d[3] > d[5]:
    print('{} é o maior'.format(d[3]))
elif d[4] > d[0] and d[4] > d[1] and d[4] > d[2] and d[4] > d[3] and d[4] > d[5]:
    print('{} é o maior'.format(d[4]))
else:
    print('{} é o maior'.format(d[5]))
if d[0] < d[1] and d[0] < d[2] and d[0] < d[3] and d[0] < d[4] and d[0] < d[5]:
    print('{} é o menor'.format(d[0]))
elif d[1] < d[0] and d[1] < d[2] and d[1] < d[3] and d[1] < d[4] and d[1] < d[5]:
    print('{} é o menor'.format(d[1]))
elif d[2] < d[0] and d[2] < d[1] and d[2] < d[3] and d[2] < d[4] and d[2] < d[5]:
    print('{} é o menor'.format(d[2]))
elif d[3] < d[0] and d[3] < d[1] and d[3] < d[2] and d[3] < d[4] and d[3] < d[5]:
    print('{} é o menor'.format(d[3]))
elif d[4] < d[0] and d[4] < d[1] and d[4] < d[2] and d[4] < d[3] and d[4] < d[5]:
    print('{} é o menor'.format(d[4]))
else:
    print('{} é o menor'.format(d[5]))
