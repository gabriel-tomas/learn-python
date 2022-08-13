colocados = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
             'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São paulo', 'Fluminense', 'Sport Recife', 'Ec Vitória',
             'Coritiba', 'Avaí', 'Ponte preta', 'Atlético-GO')
print(f'Os cinco primeiros colocados são {colocados[0:5]}')
print(f'Os ultimos 4 são {colocados[-4:]}')
print(f'Times em ordem alfabética: {sorted(colocados)}')
print(f'O time {colocados[colocados.index("Chapecoense")]} está em {colocados.index("Chapecoense") + 1}')
