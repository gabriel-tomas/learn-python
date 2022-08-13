pessoa = []
pessoas = []
pessoa.append('Karolaine')
pessoa.append(19)

pessoas.append(pessoa[:])

pessoa[0] = 'Gabriel'
pessoa[1] = 17
pessoas.append(pessoa[:])


print(f'\033[32m{pessoa}\033[m')

pessoa[0] = 'Raissa'
pessoa[1] = 25
pessoas.append(pessoa[:])

print(pessoas)

