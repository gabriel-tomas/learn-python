precofinal = maisdemil = 0
maisbarato = 0
nomemaisbarato = ''
c = 0
while True:
    print('\033[32m' + '°' * 20 + '\033[m')
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    print('\033[32m' + 'º' * 20 + '\033[m')
    c = c + 1
    precofinal += preco
    if preco > 1000:
        maisdemil += 1
    if c == 1 or preco < maisbarato:
        maisbarato = preco
        nomemaisbarato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).upper()[0]
    if continuar == 'N':
        break
print(f'O total gasto foi R${precofinal:.2f}')
print(f'Existe {maisdemil} produtos mais de R$1000')
print(f'O produto mais barato foi {nomemaisbarato} que custou R${maisbarato:.2f}')
