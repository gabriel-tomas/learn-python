tup = (int(input('Digite um valor: ')),
        int(input('Digite outro valor: ')),
        int(input('Digite outro valor: ')),
        int(input('Digite o último valor: ')))
print(f'Apareceu {tup.count(9)} vezes o valor 9')
if tup.count(3) != 0:
    print(f'O número 3 aparece primeira vez na posição {tup.index(3) + 1}')
print('Números pares: ', end='')
for c in tup:
    if c % 2 == 0:
        print(c, end=' ')
print(f'\n{"Fim do programa":=^50}')
