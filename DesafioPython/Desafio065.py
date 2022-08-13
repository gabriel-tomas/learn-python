continuar = 'S'
todosnum = 0
divdenum = 0
maior = 0
menor = 0
cont = 0
while continuar != 'N':
    n = int(input('Digite o valor: '))
    cont = cont + 1
    if cont == 1:
        maior = n
    if n > maior:
        maior = n
    if cont == 1:
        menor = n
    if n < menor:
        menor = n
    todosnum = todosnum + n
    divdenum = divdenum + 1
    continuar = str(input('Quer continuar [S/N]?')).upper()
print('Você digitou {} números e a média entre os valores é {}'.format(cont, todosnum / divdenum))
print('O maior é {} e o menor é {}'.format(maior, menor))
