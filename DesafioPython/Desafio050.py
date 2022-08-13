r = 0
for c in range(1, 7):
    n = int(input('Digite o número inteiro: '))
    if n % 2 == 0:
        r = r + n
print('A soma apenas dos pares é {}'.format(r))
