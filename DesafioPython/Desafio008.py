cores = {'azul': '\033[34m', 'vermelho': '\033[31m', 'amarelo': '\033[33m', 'verde': '\033[32m'}
metros = float(input('{}Diga o valor em metros: '.format(cores['azul'])))
centimetros = metros*100
milimetros = centimetros*10
print('{}Em Quilometros {}{}\n{}Em Hectometros {}{}\n{}Em Decametros {}{}'
      '\n{}Em Decímetros {}{}\nEm centímetros {}\nEm milimetros {}'
      .format(cores['verde'], (metros/1000), '\033[m', cores['amarelo'], (metros/100), '\033[m',
              cores['vermelho'], (metros/10), '\033[m', '\033[35m', (metros*10), '\033[m',
              '\033[37m', centimetros, '\033[34m', milimetros))
