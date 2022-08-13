from datetime import date
ano = int(input('Digite o ano de nascimento: '))
ano1 = str(date.today()).split('-')
idadef = int(ano1[0]) - ano
print('O atleta tem {} anos de idade a categoria é: '.format(idadef), end='')
if idadef <= 9:
    print('Mirim')
elif idadef in range(9, 15):
    print('Infantil')
elif idadef in range(15, 20):
    print('Junior')
elif idadef >= 20 and idadef <=25:
    print('Sênior')
else:
    print('Master')
