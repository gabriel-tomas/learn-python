lista = [0, 2, 10, 3, 31]
del lista[0]
lista.insert(0, 10)
lista.append(22)
lista.sort(reverse = True)
lista.remove(31)
lista.append(24)
print(lista.index(24))
if 24 in lista:
    lista.remove(24)
    print('O valor 24 existe e foi removido')
elif 24 not in lista:
    print('Não existe o valor 24 na lista')
print(lista)