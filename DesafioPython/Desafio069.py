pmaisdezoito = homens = mulheresmenosvinte = 0
while True:
    print('~' * 23)
    idade = int(input('Digite a idade: '))
    sexo = 'g'
    while sexo not in 'MmFf':
        sexo = str(input('Digite o sexo [M/F]: '))
        print(sexo)
    print('~' * 23)
    if idade > 18:
        pmaisdezoito = pmaisdezoito + 1
    if sexo == 'm':
        homens = homens + 1
    if sexo == 'f' and idade < 20:
        mulheresmenosvinte = mulheresmenosvinte + 1
    continuar = str(input('Quer continuar [S/N]? ')).lower()
    if continuar == 'n':
        break
print(f'{pmaisdezoito} pessoas com mais de dezoito anos.'
      f'\n{homens} Homens cadastrados.'
      f'\n{mulheresmenosvinte} mulheres com menos de vinte anos. ')
