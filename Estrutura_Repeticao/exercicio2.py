nota = int(input('Digite uma nota: '))

while (nota > 10) or (nota < 0):
    print('Valor invalido, digite novamente')
    nota = int(input('Digite uma nota: '))
else:
    print('Valor Valido')
