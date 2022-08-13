frase = str(input('Digite uma frase: ')).lower()
rep = frase.replace(' ', '')
inverso = ''
for inv in range(len(rep)-1, -1, -1):
    print(rep[inv], end='')
    inverso = inverso + rep[inv]
print('\n{}\nÉ um palíndromo'.format(rep) if rep == inverso else '\n{}\nNão é um palíndromo'.format(rep))
