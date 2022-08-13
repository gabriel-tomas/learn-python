lista = []
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print('Adicionado')
    else:
        print('Esse número não foi adicionar, pois é repetido')
    continuar = str(input('Continuar [S/N]? ')).upper()[0]
    if continuar in 'N':
        break
print(f'Os números digitados foram {lista}')
lista.sort()
print(lista)
