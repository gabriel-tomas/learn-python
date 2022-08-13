nota1 = float(input('\033[mDigite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
notaf = (nota1+nota2)/2
print('A média do aluno é \033[4;1;32m{}\033[m'.format(notaf) if notaf >= 6
      else 'A média do aluno é \033[4;1;31m{}\033[m'.format(notaf))
