lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Inserido ao final da lista')
    else:
        posicao = 0
        while True:
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                print(f'Inserido na posição {posicao}')
                break
            posicao += 1
print(f'Lista: {lista}')
