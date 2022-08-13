peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
IMC = peso / (altura ** 2)
print('Seu IMC é {:.1f} você '.format(IMC), end='')
if IMC < 18.5:
    print('está: Abaixo do peso')
elif IMC <= 25:
    print('está com: Peso ideal')
elif IMC <= 30:
    print('está com: Sobrepeso ')
elif IMC <= 40:
    print('está com: Obesidade')
else:
    print('está com: Obesidade mórbida')
