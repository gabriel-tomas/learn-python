while True:
    n = int(input('Quer ver tabuada de qual número? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {n} = {c * n}')
print('Programa encerrado.')
