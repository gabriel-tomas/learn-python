from math import cos, tan, sin, radians
angulo1 = int(input('\033[32mDiga o angulo: \033[m'))
angulo = radians(angulo1)
print('\033[33mSeno = \033[m\033[33;4m{:.2f}\033[m'
      '\n\033[34mCosseno = \033[m\033[34;4m{:.2f}\033[m'
      '\n\033[36mTangente = \033[m\033[36;4m{:.2f}\033[m'.format(sin(angulo), cos(angulo), tan(angulo)))
