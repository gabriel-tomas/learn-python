print('{}'.format('\033[31mJol\033[33mas \033[34mde \033[35mTopr\033[36mudos\033[m'))
produto = float(input('Digite o preço do produto: R$'))
pagamento = str(input("""[ 1 ]- à vista no dinheiro 10% de desconto
[ 2 ]- à vista no cartão 5% de desconto
[ 3 ]- 2x no cartão preço normal
[ 4 ]- 3x ou mais no cartão 20% de juros
Qual a forma de pagamento? """))
if pagamento == '1':
    print('\nCom 10% de desconto avista no dinheiro ficou por R${:.2f}'.format(produto-(produto*10/100)))
elif pagamento == '2':
    print('\nCom 5% de desconto no cartão a vista ficou por R${:.2f}'.format(produto-(produto*5/100)))
elif pagamento == '3':
    print('\n2x no cartão R${:.2f}'.format(produto/2))
elif pagamento == '4':
    parcelamento = int(input('\nDigite quantas vezes no cartão: '))
    print('O preço final com 20% de juros ficou'
          ' por R${:.2f} parcelado em {} vezes'.format(((produto*20/100)+produto)/parcelamento, parcelamento))
else:
    print('Erro \033[31mOPÇÃO INVALIDA')
