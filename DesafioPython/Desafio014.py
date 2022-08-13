temperatura = float(input('\033[35mDiga a temperatura em Celsius: \033[m'))
print('\033[35mEm Fahrenheit \033[31m{:.1f}F'.format((temperatura*9/5)+32)
      , '\n\033[35mEm Kelvin \033[31m{:.1f}K'.format(temperatura+273))
