
ex = str(input('Digite a expressão: '))
parenteses = []
for n in range(0, len(ex)):
    if ex[n] in '()':
        parenteses.append(ex[n])
cont = [parenteses.count('('), parenteses.count(')')]
if (cont[0] + cont[1]) % 2 == 0:
    print(f'Expressão válida.')
else:
    print(f'Expressão inválida.')
