primeira_lista = []
lista_par = []
lista_impar = []
for valores in range(0, 7):
    valor = int(input('Digite um valor inteiro: '))
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)
primeira_lista.append(lista_par[:])
primeira_lista.append(lista_impar[:])
del lista_par, lista_impar
print(f'\033[32mLista \033[1moriginal\033[m: {primeira_lista}')
primeira_lista[0].sort()
primeira_lista[1].sort()
print(f'\033[32mLista em ordem \033[1mcrescente\033[m:\n'
      f'\033[35mPares\033[m: {primeira_lista[0]}\n'
      f'\033[35mÍmpares\033[m: {primeira_lista[1]}')
