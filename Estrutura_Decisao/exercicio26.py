litros = int(input('Digite a quantidade de litros: '))

print('Tipo de combustivel: ')

print('''A --> Álcool
G -->Gasolina''')

alco_gaso = ''

tipo = str(input(''))

tipo_comb = tipo.upper()


if (tipo_comb == 'A'):
    if (litros <= 20):
        preco = litros * 1.90
        preco_disc = preco * 0.03
        valor_total = preco - preco_disc
        alco_gaso = 'Álcool'

    elif (litros > 20):
        preco = litros * 1.90
        preco_disc = preco * 0.05
        valor_total = preco - preco_disc
        alcool = 'Álcool'

if (tipo_comb == 'G'):
    if (litros <= 20):
        preco = litros * 2.50
        preco_disc = preco * 0.04
        valor_total = preco - preco_disc
        alco_gaso = 'Gasolina'

    elif (litros > 20):
        preco = litros * 2.50
        preco_disc = preco * 0.06
        valor_total = preco - preco_disc
        alco_gaso = 'Gasolina'

print(
    f'Quantidade de litros: {litros}: de {alco_gaso} com desconto de: {preco_disc}. Total: {valor_total}')
