price1 = float(input('Qual preço do 1° produto: '))
price2 = float(input('Qual preço do 2° produto: '))
price3 = float(input('Qual preço do 3° produto: '))

menor = price1

if (price2 < menor):
    menor = price2
if (price3 < menor):
    menor = price3

print(f'O produto de menor valor: {menor}')
