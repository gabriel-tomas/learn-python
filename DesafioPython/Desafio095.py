dicio = {}
list_quant_gol = []
list_jogadores = []
dic_df = {}
total_gols = 0

while True:
    print('-=-' * 25)
    dicio['nome'] = str(input('Nome: '))
    num_parts = int(input(f'Numéro de partidas de {dicio["nome"]}: '))
    for num_part in range(1, num_parts + 1):
        quant_gol = int(input(f'Gols na partida {num_part}: '))
        total_gols += quant_gol
        list_quant_gol.append(quant_gol)
    dicio['num_gols'] = list_quant_gol[:]
    dicio['total'] = total_gols
    list_quant_gol.clear()
    total_gols = 0
    list_jogadores.append(dicio.copy())
    conti = str(input('Continuar [S/N]? '))
    if conti in 'Nn':
        break
print('-=-' * 25)
print(f'{"cod":<5} {"nome":<10} {"gols":<25}{"total":<35}')
print(f'--' * 23)
for i, jogad in enumerate(list_jogadores):
    print(f'{i + 1:<5} {jogad["nome"]:<10} {str(jogad["num_gols"]):<25}{jogad["total"]:<35}')
while True:
    most_dados = int(input('Mostrar dados de qual jogador? ')) - 1
    print(most_dados, len(list_jogadores))
    if most_dados < 0:
        break
    elif most_dados >= len(list_jogadores):
        print(f'\033[31mJogador {most_dados + 1} Não existe\033[m')
    else:
        gols = list_jogadores[most_dados]['num_gols']
        print(f'=> Dados do jogador {list_jogadores[most_dados]["nome"]}:')
        for i, gol in enumerate(gols):
            print(f'    Na partida {i + 1} fez {gol} gols.')
