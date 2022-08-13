frase = str(input('\033[33mDigite a frase: ')).strip()
print('Aparece \033[4;32m{}\033[m \033[33mvezes a letra "A"'.format(frase.lower().count('a')))
print('Aparece primeira vez na \033[32;4m{}\033[m \033[33mletra'.format(frase.lower().find('a') + 1))
print('Aparece pela ultima vez na \033[32;4m{}\033[m \033[33mletra'.format(frase.lower().rfind('a') + 1))
