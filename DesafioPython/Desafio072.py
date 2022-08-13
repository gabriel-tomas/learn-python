numexte = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre o 0 e 20: '))
    print(f'O número digitado foi {numexte[num]}')
    while True:
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break

