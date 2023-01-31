l1 = int(input('Digite o lado 1 do triangulo: '))
l2 = int(input('Digite o lado 2 do triangulo: '))
l3 = int(input('Digite o lado 3 do triangulo: '))


triangulo = l1 + l2

if (triangulo > l3):
    if (l1 == l2 and l2 == l3):
        print('Isso é um triangulo equilatero')
    elif (l1 == l2 or l1 == l3 or l2 == l3 or l2 == l1 or l3 == l1 or l3 == l2):
        print('Isso é um Triângulo Isósceles')
    elif (l1 != l2 and l2 != l3):
        print('Isso é um Triângulo Escaleno')
else:
    print('Não é um triangulo')
