v_carro = float(input('\033[1;37mDigite a velocidade do carro \033[4mKm/h:\033[m '))
if v_carro > 80:
    print('\033[31mVocê foi multado por \033[4mEXCESSO DE VELOCIDADE\033[m')
    print('\033[31mTerá que ser pago \033[4;33mR${:.2f}'.format((v_carro-80)*7))
else:
    print('Teve sorte hoje ein!')