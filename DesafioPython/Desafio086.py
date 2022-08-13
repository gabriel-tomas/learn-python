'''coluna = linha = 0
lista = []
lista2 = []
for valores in range(0, 9):
    valor = int(input(f'Digite um valor para a posição {linha, coluna}: '))
    coluna += 1
    if coluna == 3:
        coluna = 0
        linha += 1
    lista2.append(valor)
    if len(lista2) == 3:
        lista.append(lista2[:])
        lista2.clear()
print('=-'*20)
for linhas in lista:
    for num in linhas:
        print(f'\033[34m[ \033[31m{num:^3}\033[m \033[34m]', end='\033[m')
    print('\n', end='')'''
lista = [[], [], []]
linha = 0
for valores in range(0, 9):
    lista[linha].append(int(input(f'Digite um valor: ')))
    if len(lista[linha]) == 3:
        linha += 1
for linhas_matriz in lista:
    for numero in linhas_matriz:
        print(f'( {numero:^3} )', end='')
    print()
