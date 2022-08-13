from random import randint
vitorias = 0
while True:
    print('~' * 20)
    n = int(input('Digite o valor: '))
    pi = str(input('Par ou ímpar? [p/i] ')).lower()
    cpu = randint(1, 10)
    jogada = cpu + n
    if pi == 'p':
        if jogada % 2 == 0:
            print(f'Você jogou {n} e o CPU {cpu} o número deu {jogada} Par e você VENCEU!')
            vitorias = vitorias + 1
        else:
            print(f'Você jogou {n} e o CPU {cpu} o número deu {jogada} Ímpar e você PERDEU.')
            break
    elif pi == 'i':
        if jogada % 2 != 0:
            print(f'Você jogou {n} e o CPU {cpu} o número deu {jogada} Ímpar e você VENCEU!')
            vitorias = vitorias + 1
        else:
            print(f'Você jogou {n} e o CPU {cpu} o número deu {jogada} Par e você PERDEU.')
            break
print('~' * 20)
print(f'Você venceu {vitorias} vezes consecutivas.')
