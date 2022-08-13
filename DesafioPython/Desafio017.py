from math import hypot
ca = float(input('\033[35mDigite a medida do cateto adjascente: \033[m'))
co = float(input('\033[35mDigite a medida do cateto oposto: \033[m'))
print('\033[37mA hipotenusa é igual a \033[m\033[1;34;4m{:.2f}'.format(hypot(ca, co)))
