lista_num = []
maior = menor = 0
posicaomaior = []
posicaomenor = []
for p in range(0, 5):
    a = int(input(f'Digite um número na posição {p}: '))
    lista_num.append(a)
    if p == 0 or a > maior:
        maior = a
    if p == 0 or a < menor:
        menor = a
for i, valor in enumerate(lista_num):
    if valor == maior:
        posicaomaior.append(i)
    if valor == menor:
        posicaomenor.append(i)
print(f'Sua lista de números: {lista_num}')
print(f'Maior número: {maior} posição: {posicaomaior}')
print(f'Menor valor: {menor} posição {posicaomenor}')
