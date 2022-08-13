a = 0
b = 0
for c in range(0, 501, 3):
    if c % 2 != 0:
        a = a + c
        b = b + 1
        print(c)
print('A soma é {}'.format(a))
print('Foram {} itens no total somados'.format(b))
