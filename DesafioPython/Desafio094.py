list_pessoas = []
list_mulheres = []
list_acima_media = []
dicio = {}
while True:
    dicio['nome'] = str(input('Nome: '))
    while True:
        dicio['sexo'] = str(input('Sexo: [M/F] '))
        if dicio['sexo'] in 'mfMF':
            break
        else:
            print(f'\033[31mERRO, digite apenas M/m ou F/f\033[m')
    dicio['idade'] = int(input('Idade: '))
    list_pessoas.append(dicio.copy())
    while True:
        cont = str(input('Continuar? [S/N] '))
        if cont in 'SNsn':
            break
        else:
            print(f'\033[31mERRO, digite apenas S/s ou N/n\033[m')
    if cont in 'Nn':
        break
print('-=-' * 35)
print('Informações: ')
total_pessoas = len(list_pessoas)
som_idade = 0
print(f'    >Foram cadastradas: {total_pessoas} pessoas')
for pessoas in list_pessoas:
    som_idade += pessoas['idade']
    if pessoas['sexo'] in 'Ff':
        list_mulheres.append(pessoas['nome'])
media = som_idade / total_pessoas
print(f'    >Média de idade: {media:.2f}')
print('    >Lista de mulheres cadastradas: ', end='')
for mulheres in list_mulheres:
    print(mulheres, end=' ')
print()
for pessoas_acima_media in list_pessoas:
    if pessoas_acima_media['idade'] > media:
        list_acima_media.append(pessoas_acima_media)
print('    >Pessoas acima da média: ')
for pessoas_acima in list_acima_media:
    print(f'        Nome: {pessoas_acima["nome"]}, Sexo: {pessoas_acima["sexo"].upper()}, Idade: {pessoas_acima["idade"]}')
