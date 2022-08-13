nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
notaf = (nota1+nota2)/2
print('A média foi {}'.format(notaf))
if notaf < 5:
    print('\033[31mREPROVADO\033[m')
elif notaf >= 5 and notaf < 7:
    print('\033[34mRECUPERAÇÃO\033[m')
else:
    print('\033[32mAPROVADO')
