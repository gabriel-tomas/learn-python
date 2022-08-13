lista_principal = []
lista_nome_notas = []
lista_notas = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    lista_nome_notas.append(nome)
    lista_notas.append(nota1)
    lista_notas.append(nota2)
    lista_nome_notas.append(lista_notas[:])
    lista_notas.clear()
    lista_principal.append(lista_nome_notas[:])
    lista_nome_notas.clear()
    continuar = str(input('Continuar [S/N]? '))
    if continuar in 'Nn':
        break
print(lista_principal)
print('-'*26)
print('\033[36mNum. Nome         Média')
for indice, dados_pessoas in enumerate(lista_principal):
    print(f'\033[32m{indice + 1}\033[m', end='')
    print(f'\033[33m{dados_pessoas[0]:^13}\033[m', end='')
    print(f'\033[34m{(dados_pessoas[1][0] + dados_pessoas[1][1]) / 2:^15.1f}\033[m')
print('-'*26)
while True:
    exibir = str(input('Mostrar notas de qual pessoa: '))
    if exibir.isnumeric() == True:
        print(f'\033[34m{lista_principal[int(exibir) - 1][1]}\033[m')
    for dados_principal in lista_principal:
        for dados in dados_principal:
            if dados == exibir.title():
                print(f'\033[34m{dados_principal[1]}\033[m')
    mais = str(input('Ver mais [S/N]? '))
    if mais in 'Nn':
        break
