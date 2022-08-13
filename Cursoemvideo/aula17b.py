valor = []
for n in range(0, 3):
    valor.append(int(input('Digite o valor: ')))
print(valor)
for i in range(0, len(valor)):
    print(f'{valor[i]} na posição {i}')
for n in range(0, 1):
    valor.remove(int(input('Digite o valor para ser retirado: ')))
print(valor)
