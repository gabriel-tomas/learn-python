nome = str(input('Diga seu nome: ')).lower().strip()
if nome == 'gabriel':
    print('Que nome bonito')
elif nome in 'maria pedro joão':
    print('Seu nome é popular')
else:
    print('Seu nome é muito normal')