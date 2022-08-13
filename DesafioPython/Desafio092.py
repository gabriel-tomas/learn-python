from datetime import date
dic = {}
ano_atual = date.today().year
nome = str(input('Nome: '))
idade = ano_atual - int(input('Ano de nascimento: '))
cart_trab = int(input('Carteira de trabalho(0, caso não tenha): '))
dic['nome'], dic['idade'], dic['carteira'] = nome, idade, cart_trab
if cart_trab != 0:
    ano_contra = int(input('Ano de contratação: '))
    salario = float(input('Salário: R$'))
    dic['ano de contratação'], dic['salario'] = ano_contra, salario
    dic['aposentadoria'] = 35 - (ano_atual - ano_contra) + dic['idade']
print('+=' * 30)
for keys, values in dic.items():
    print(f'   - {keys} é igual {values}')
