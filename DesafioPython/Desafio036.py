valorC = float(input('Digite o valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
q_anos = int(input('Quantos anos ele vai pagar a casa? '))
prestacao = valorC/(q_anos*12)
salario_calculo = salario*30/100
if prestacao > salario_calculo:
    print('\033[31memprestimo negativado')
else:
    print('Vai ter que ser pago R${:.2f} todos os meses durante {} anos'.format(prestacao, q_anos))
