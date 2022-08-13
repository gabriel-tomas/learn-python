n1 = 0
nstotal = 0
n = 0
while n != 999:
    n = int(input('Digite o valor: '))
    if n != 999:
        nstotal = nstotal + 1
        n1 = n1 + n
print('A soma entre eles é {} e foram digitados {} números'.format(n1, nstotal))
