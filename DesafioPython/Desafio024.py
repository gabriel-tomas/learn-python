nome_cidade = str(input('\033[34mDiga o nome de sua cidade: ').strip())
a = nome_cidade.split()
b = a[0].lower()
if 'santo' in b:
    print('\033[32mTrue')
else:
    print('\033[31mFalse')
