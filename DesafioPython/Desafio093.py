dicio = {}
list_quant_gol = []
total_gols = 0

nome = str(input('Nome: '))
num_parts = int(input('Numéro de partidas: '))
for num_part in range(1, num_parts + 1):
    quant_gol = int(input(f'Gols na partida {num_part}: '))
    list_quant_gol.append(quant_gol)
dicio['nome'] = nome
dicio['quantidade_gols'] = list_quant_gol[:]
dicio['total'] = sum(list_quant_gol)
print(dicio)
print('='*60)
for k, v in dicio.items():
    if k == 'nome':
        print(f'O jogador {v} jogou {len(dicio["quantidade_gols"])} partidas:')
    elif k == 'quantidade_gols':
        for i, gol in enumerate(v):
            print(f'   >Na partida {i + 1} ele fez {gol}')
    else:
        print(f'O total de gols foi {v}')

#for keys, values in dicio.items():
#    if keys == 'quantidade_gols':
#        for val in values:
#            print(val)
