km = float(input('\033[32mQuantos Km foram rodados? '))
dias = int(input('Quantos dias foi alugados? \033[m'))
print('\033[32mO preço a pagar pelos dias e Km rodados: \033[33mR${:.2f}'.format(dias*60+km*0.15))
