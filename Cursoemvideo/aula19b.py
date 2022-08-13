estado = {}
brasil = []
for estados in range(0, 4):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla '] = str(input('Sigla: '))
    brasil.append(estado.copy())
for estados in brasil:
    for keys, values in estados.items():
        print(f'{keys} = {values}')
    print()
