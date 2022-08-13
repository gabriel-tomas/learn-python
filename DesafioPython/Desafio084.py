lista = []
pessoas_cadastradas = maiorpeso = menorpeso = 0
while True:
    nome = str(input('Digite seu nome> '))
    peso = float(input('Digite seu peso> '))
    pessoas_cadastradas += 1
    lista.append([nome, peso])
    continuar = str(input('Continuar [S/N]? '))
    if continuar in 'Nn':
        break
print('='*40)
print(f'Foram cadastradas {len(lista)} pessoas\n')
print('Pessoas mais pesadas:')
for indice, dados_pessoas in enumerate(lista):
    if indice == 0 or dados_pessoas[1] >= maiorpeso:
        maiorpeso = dados_pessoas[1]
for pessoas in lista:
    if pessoas[1] == maiorpeso:
        print(f'{pessoas[0]} com {pessoas[1]}')
print('\nPessoas mais leves:')
for indice, dados_pessoas in enumerate(lista):
    if indice == 0 or dados_pessoas[1] <= menorpeso:
        menorpeso = dados_pessoas[1]
for pessoas in lista:
    if pessoas[1] == menorpeso:
        print(f'{pessoas[0]} com {pessoas[1]}')
