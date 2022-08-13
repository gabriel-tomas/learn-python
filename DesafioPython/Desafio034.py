salario = float(input('\033[36mDigite o sálario do funcionário R$\033[m'))
if salario > 1250.00:
    salariof = (10*salario/100)+salario
    desconto = 10
else:
    salariof = (15*salario/100)+salario
    desconto = 15
print('\033[34mO salário final com \033[1;4m{}%\033[m \033[34mde aumento é de \033[1;4;33mR${}'.format(desconto, salariof))
