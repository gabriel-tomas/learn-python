n = int(input('\033[1;36mDiga o número: '))
print('\033[:36mO sucessor de {}{}{} \033[36mé\033[31m {} \033[36me seu antecessor é\033[31m {}'.format('\033[32m', n, '\033[m', (n+1), (n-1)))
