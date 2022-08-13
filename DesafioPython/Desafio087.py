coluna = linha = 0
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

soma_valores_pares = soma_terceira_coluna = 0
maiorvalordasegundalinha = 0
for indice, linhas in enumerate(lista):
    for indicecoluna, num in enumerate(linhas):
        print(f'\033[34m[ {num} ]', end='\033[m')
        if num % 2 == 0:
            soma_valores_pares += num
        if indicecoluna == 2:
            soma_terceira_coluna += num
    if indice == 1:
        for indicesegundalinha, nums in enumerate(lista[1]):
            if indicesegundalinha == 0 or nums > maiorvalordasegundalinha:
                maiorvalordasegundalinha = nums
    print('\n', end='')

print('=-'*20)
print(f'\033[35mSoma dos valores pares: \033[1m{soma_valores_pares}\033[m\n'
      f'\033[35mSoma da terceira coluna: \033[1m{soma_terceira_coluna}\033[m\n'
      f'\033[35mMaior valor da segunda linha: \033[1m{maiorvalordasegundalinha}\033[m\n')
