itens = ('Cachorro-quente', 2.50, 'Pão', 2, 'Leite', 5.32, 'Feijoada', 10.43, 'Pastel', 3.40, 'Coxinha', 1.20)
for el in range(0, len(itens)):
    if el % 2 == 0:
        print(f'{itens[el]:.<25}', end='')
    else:
        print(f'R${itens[el]:>6.2f}')

