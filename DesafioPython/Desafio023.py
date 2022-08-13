n = input('\033[32mDigite um número: ')
n1 = int(n) // 1 % 10
n2 = int(n) // 10 % 10
n3 = int(n) // 100 % 10
n4 = int(n) // 1000 % 10
print('\033[32mUnidade: \033[m\033[31m{}\033[m'
      '\n\033[32mDezena: \033[m\033[31m{}\033[m\n'
      '\033[32mCentena: \033[m\033[31m{}'
      '\n\033[32mMilhar: \033[m\033[31m{}'.format(n1, n2, n3, n4))
