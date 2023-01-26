numero_inteiro = int(input('Digite um numero inteiro: '))
numero_inteiro2 = int(input('Digite um numero inteiro: '))
numero_real = float(input('Digite um numero real: '))

dobro_primeiro = numero_inteiro * 2
metade_segundo = numero_inteiro2 / 2

soma_numeros = dobro_primeiro + metade_segundo

triplo_primeiro = numero_inteiro * 3
soma_numeros2 = triplo_primeiro + numero_real

terceiro_cubo = numero_real ** 3

print(f'O produto do dobro do primeiro com metade do segundo: {soma_numeros}')
print(f'A soma do triplo do primeiro com o terceiro: {soma_numeros2}')
print(f'O terceiro elevado ao cubo: {terceiro_cubo}')
