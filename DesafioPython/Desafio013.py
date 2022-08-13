salario1 = float(input('\033[34mSalário do funcionario: \033[32mR$'))
print('\033[34mO salário com \033[4m15%\033[m\033[34m'
      ' de aumento ficou com \033[32mR$\033[33m{:.2f}'.format(salario1+(salario1*15/100)))
