import math

a = int(input('Digite o Valor de A: '))
b = int(input('Digite o Valor de B: '))
c = int(input('Digite o Valor de C: '))

delta = (b ** 2) - (4 * a * c)
raiz = math.sqrt(delta)
if (a != 0):
    if (delta > 0):
        x1 = -b + raiz
        x1_2 = 2 * a
        x1_3 = x1 / x1_2

        x2 = -b - raiz / 2 * a
        x2_2 = 2 * a
        x2_3 = x2 / x2_2
        print(f'delta positivo possui 2 valor reais, esse é: {x1_3} e {x2_3}')
    elif (delta == 0):
        x1 = (-b + raiz) / 2 * a
        print(f'delta igual a zero possui apenas 1 valor reais, esse é: {x1}')
    else:
        print('Delta negativo, a equação não possui raizes reais')
else:
    print('A igual a 0. Programa encerrado')
