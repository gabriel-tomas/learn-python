#galera = [['Maria', 23], ['Paula', 39], ['Joaquim', 23], ['Nayara', 18], ['Marcos', 48]]
#print(galera[4][0])
dados = []
nomes = []
for c in range(0, 4):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    nomes.append(dados[:])
    dados.clear()
print(nomes)
