numeros = str(input('\033[33mDigite os numeros separados por espaço: \033[m'))
n_split = numeros.split()
if int(n_split[2]) < int(n_split[0]) and int(n_split[2]) < int(n_split[1]):
    menor = n_split[2]
if int(n_split[0]) < int(n_split[1]) and int(n_split[0]) < int(n_split[2]):
    menor = n_split[0]
if int(n_split[1]) < int(n_split[0]) and int(n_split[1]) < int(n_split[2]):
    menor = n_split[1]
if int(n_split[0]) > int(n_split[1]) and int(n_split[0]) > int(n_split[2]):
    maior = n_split[0]
if int(n_split[2]) > int(n_split[1]) and int(n_split[2]) > int(n_split[0]):
    maior = n_split[2]
if int(n_split[1]) > int(n_split[0]) and int(n_split[1]) >int(n_split[2]):
    maior = n_split[1]
print('\033[34mO menor número é \033[4m{}\033[m\n\033[34mE o maior \033[4m{}'.format(menor, maior))
