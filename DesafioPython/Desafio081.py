list = []
while True:
    list.append(int(input('Valor: ')))
    continuar = str(input('Continuar [S/N]? '))
    if continuar in 'Nn':
        break
list.sort(reverse=True)
print(f'Foram digitados {len(list)} números'
      f'\nNa forma decrescente fica {list}')
if 5 in list:
    print(f'O valor 5 se encontra na lista')
else:
    print(f'O valor 5 não se encontra na lista')
