dicionario = {}
nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))
dicionario['nome'], dicionario['media'] = nome, media
if media >= 7:
    dicionario['situação'] = 'Aprovado'
elif 5 <= media < 7:
    dicionario['situação'] = 'Recuperação'
elif 5 > media:
    dicionario['situação'] = 'Reprovado'
print('--' * 15)
for k, v in dicionario.items():
    print(f'    O {k} é {v}')