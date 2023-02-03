print('''Até 5 Kg                   Acima de 5 Kg 
Morango R$ 2,50 por Kg     R$ 2,20 por Kg 
Maçã R$ 1,80 por Kg        R$ 1,50 por Kg''')

kg_mor = int(input('Digite a quantidade em Kg de morangos: '))
kg_mac = int(input('Digite a quantidade em Kg de Maças: '))

kg_total = kg_mor + kg_mac

if (kg_mor <= 5):
    kg_totMor = kg_mor * 2.50
elif (kg_mor > 5):
    kg_totMor = kg_mor * 2.20

if (kg_mac <= 5):
    kg_totmac = kg_mac * 1.80
elif (kg_mac > 5):
    kg_totmac = kg_mac * 1.50

valor_total = kg_totMor + kg_totmac

valor_disc = valor_total

if (kg_total > 8 or valor_total > 25):
    kg_valdesc = valor_total * 0.10
    valor_disc = valor_total - kg_valdesc

print(f'Você comprou {kg_mor}kg de morango e {kg_mac}kg de maças. Peso total: {kg_total}kg. Valor sem desconto: {valor_total} R$. Valor com desconto: {round(valor_disc)} R$')
