preco = float(input('\033[1;30;46mDiga o preço do produto: \033[1mR$'))
desconto = int(input('Diga o desconto: \033[1m%\033[m'))
rfinal = preco-(preco*desconto/100)
print('\033[32mO preço era \033[33mR${:.2f}\033[32m e ficou por \033[33mR${:.2f}'.format(preco, rfinal))
