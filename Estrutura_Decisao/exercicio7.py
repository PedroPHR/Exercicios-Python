number1 = int(input('Inserir 1° numero: '))
number2 = int(input('Inserir 2° numero: '))
number3 = int(input('Inserir 3° numero: '))

maior = number1
menor = number1


if (number2 > maior):
    maior = number2
if (number3 > maior):
    maior = number3

if (number2 < menor):
    menor = number2
if (number3 < menor):
    menor = number3


print(f'O maior numero é: {maior}')
print(f'O menor numero é: {menor}')
