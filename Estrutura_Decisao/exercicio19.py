inteiro = int(input('Digite um numero: '))

sobras_deze = inteiro % 100
sobras_unid = inteiro % 10
centenas = inteiro // 100
dezenas = sobras_deze // 10


if (inteiro <= 1000):
    print(f'{inteiro} = {centenas} Centenas, {dezenas} Dezenas e {sobras_unid} Unidades')
else:
    print('Numero inteiro maior que 1000')
