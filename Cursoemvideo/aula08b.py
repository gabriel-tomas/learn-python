num = int(input('Digite um número: '))
from math import sqrt, ceil
r_num = sqrt(num)
r2_num = ceil(r_num)
print('A raíz de {} é igual a {:.2f}'.format(num, r2_num))
