distancia_de_viagem = int(input('\033[7;1;45mDigite a distância da viagem em Km: \033[m'))
preco = 0.50 * distancia_de_viagem if distancia_de_viagem <= 200 else 0.45 * distancia_de_viagem
print('\033[35mPara \033[4m{}km\033[m \033[35mo preço é \033[33m{:.2f}R$'.format(distancia_de_viagem, preco))
