lista = list()
listpar = []
listimpar = []
while True:
    n = int(input('Digite o número: '))
    lista.append(n)
    continuar = str(input('Continuar? '))
    if continuar in 'Nn':
        break
for el in lista:
    if el % 2 == 0:
        listpar.append(el)
    else:
        listimpar.append(el)
print(f'Lista normal: {lista}')
print(f'Lista par: {listpar}')
print(f'Lista impar: {listimpar}')
