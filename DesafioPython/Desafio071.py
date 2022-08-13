n = int(input('Qual sera o valor sacado? R$'))
valor = n
contcinquenta = 0
contvinte = 0
contdez = 0
contum = 0
while True:
    if n // 50 != 0:
        valor = valor - 50
        contcinquenta += 1
        if valor - 50 < 0:
            break
    else:
        break
print('=' * 20)
if contcinquenta >= 1:
    print(f'{contcinquenta} notas de R$50')
while True:
    if valor // 20 != 0:
        valor = valor - 20
        contvinte += 1
        if valor - 20 < 0:
            break
    else:
        break
if contvinte >= 1:
    print(f'{contvinte} notas de R$20')
while True:
    if valor // 10 != 0:
        valor = valor - 10
        contdez += 1
        if valor - 10 < 0:
            break
    else:
        break
if contdez >= 1:
    print(f'{contdez} notas de R$10')
while True:
    if valor // 1 != 0:
        valor = valor - 1
        contum += 1
        if valor - 1 < 0:
            break
    else:
        break
if contum >= 1:
    print(f'{contum} moedas de R$1')
print('=' * 20)
