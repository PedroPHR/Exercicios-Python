import math

tamanho = float(
    input('Digite o tamanho em metros quadrados da area a ser pintada: '))
quantidade_tintas = tamanho / 3

qt = quantidade_tintas / 18

quanti_arre = math.ceil(qt)
preco_total = quanti_arre * 80
price = math.ceil(preco_total)

print(f'Quantidade de tintas necessarias para essa parede: {quanti_arre}')

print(f'Preço para adquirir as latas: {price}')
