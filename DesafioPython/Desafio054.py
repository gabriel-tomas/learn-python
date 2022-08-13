from datetime import date
contador1 = 0
contador2 = 0
for pessoas in range(1, 8):
    p = int(input('Digite o ano de nascimento da {} pessoa: '.format(pessoas)))
    if date.today().year - p < 19:
        contador1 = contador1 + 1
    else:
        contador2 = contador2 + 1
print('Tem {} pessoas mais novas\nE {} pessoas mais velhas'.format(contador1, contador2))
