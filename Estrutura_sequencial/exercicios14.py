peso_peixes = float(input('Qual peso do peixe: '))

if peso_peixes > 50:
    excesso = peso_peixes - 50
    multa = excesso * 4
    print(f'Excedeu: {excesso}, multa de {multa}')

print('Peixe não excedeu o peso estabelecido')
