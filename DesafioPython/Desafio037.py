num = int(input('Digite um número inteiro: '))
print('Conversão:\n["1"] Para BINÁRIO\n["2"] Para Octal\n["3"] Para Hexadecimal')
escolha = int(input('Escolha a conversão: '))
if escolha == 1:
    print('{} para Binário é {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} para Octal é {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} para Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Escolha apenas de 1 a 3.')
