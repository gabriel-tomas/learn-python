pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 23}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(f'\033[35mDicionário: {pessoas}\033[m\n')
print(f'\033[32mValues: {pessoas.values()}\033[m')
print(f'\033[33mKeys: {pessoas.keys()}\033[m')
print(f'\033[34mItems: {pessoas.items()}\033[m')
pessoas['peso'] = 76
del pessoas['idade']
pessoas['nome'] = 'Leandro'
for keys, value in pessoas.items():
    print(keys, '=', value)