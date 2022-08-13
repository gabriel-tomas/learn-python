import random
p1_aluno = str(input('\033[32mPrimeiro aluno: '))
s2_aluno = str(input('Segundo aluno: '))
t3_aluno = str(input('Terceiro aluno: '))
q4_aluno = str(input('Quarto aluno: \033[m'))
lista = [p1_aluno, s2_aluno, t3_aluno, q4_aluno]
import time
for tempo in range(1, 5):
    time.sleep(2)
    if tempo == 1:
        print('\033[31m.\033[33m.')
    if tempo == 2:
        print('\033[31m.\033[33m.\033[34m.')
        time.sleep(3)
    if tempo == 3:
        print('\033[31m.\033[33m.\033[34m.\033[35m.')
        time.sleep(6)
    if tempo == 4:
        print('\033[31m.\033[33m.\033[34m.\033[35m.\033[36m.\033[m')
        time.sleep(3)
print('\033[32mO escolhido/a foi o/a \033[m\033[4;33m{}'.format(random.choice(lista)))
