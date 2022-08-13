input('Iniciar(clique Enter)')
altura = float(input('\033[36mDiga a altura em metros: '))
largura = float(input('\033[34mDiga a largura em metros: '))
area = largura*altura
print('\033[35mÁrea= \033[1;4m{:.1f} metros Quadrados\033[m'.format(area))
um_litro = 2
r_area_umlitro = area/um_litro
print('\033[32mIra ser necessário= \033[1;4m{} Litros de tinta'.format(r_area_umlitro))
