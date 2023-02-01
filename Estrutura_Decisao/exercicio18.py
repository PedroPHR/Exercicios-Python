print('Digite a data no formato dd/mm/aaaa')

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digite o ano: '))


if (dia <= 31):
    if (mes <= 12):
        print(f'Data: {dia}/{mes}/{ano} é uma data valida')
    else:
        print(f'Data: {dia}/{mes}/{ano} não é uma data valida')
else:
    print(f'Data: {dia}/{mes}/{ano} não é uma data valida')
