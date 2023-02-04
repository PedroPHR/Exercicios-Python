print('''\t\t\tAté 5 Kg\t\tAcima de 5 Kg
A --> File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
B --> Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
C --> Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg''')


x = str(input('Qual dessas carne você quer comprar? '))
quanti = int(input('Quantidade que deseja comprar: '))

tipo_carne = x.upper()
pre_total = 0.0
carne = ''
total_disc = 0.0
pagamento = ''
desc = 0.0

if (quanti <= 5):
    if (tipo_carne == 'A'):
        pre_total = quanti * 4.90
        carne = 'File Duplo'
    elif (tipo_carne == 'B'):
        pre_total = quanti * 5.90
        carne = 'Alcatra'
    elif (tipo_carne == 'C'):
        pre_total = quanti * 6.90
        carne = 'Picanha'

if (quanti > 5):
    if (tipo_carne == 'A'):
        pre_total = quanti * 5.80
        carne = 'File Duplo'
    elif (tipo_carne == 'B'):
        pre_total = quanti * 6.80
        carne = 'Alcatra'
    elif (tipo_carne == 'C'):
        pre_total = quanti * 7.80
        carne = 'Picanha'

tp_paga = str(
    input('Deseja pagar no cartão tabajara:\n[S] --> para sim\n[N] --> para não\n'))

tp_paga = tp_paga.upper()

if (tp_paga == 'S'):
    desc = pre_total * 0.05
    total_disc = pre_total - desc
    pagamento = 'Cartão tabajara'

if (tp_paga == 'N'):
    pagamento = 'Outro'
    total_disc = pre_total

print(
    f'Tipo de carne: {carne}, quantidade: {quanti}, preço total: {pre_total}, tipo de pagamento: {pagamento}, valor do desconto: {desc} e valor final a pagar: {total_disc}')
