ano = int(input('\033[32mDigite o ano, coloque 0 para verificar a data atual: \033[m'))
from datetime import date
r_ano = ano % 4
if ano == 0:
    ano = date.today().year
if r_ano == 0 and r_ano % 100 != 0 or r_ano % 400 == 0:
    print('\033[32;4m{}\033[m \033[32mé um ano bissexto'.format(ano))
else:
    print('\033[32;4m{}\033[m \033[32mnão é um ano bissexto'.format(ano))
