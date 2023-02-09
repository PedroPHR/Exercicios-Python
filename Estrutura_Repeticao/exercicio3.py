nome = 'Digite seu nome: '
quant = 0
sex = ''
for cara in nome:
    quant = quant + 1

while (quant < 4):
    nome = str(input('Precisa conter mais de 3 digitos: '))

idade = int(input('digite sua idade: '))

while (idade < 0) or (idade > 150):
    idade = int(input('idade invalida: '))

salario = float(input('Digite seu salario: '))

while (salario < 0):
    salario = float(input('salario invalido: '))

sexo = str(
    input('qual seu sexo, Digite M para Masculino ou F para Feminino: '))

sexo = sexo.upper()

if (sexo == 'M'):
    sex == 'Masculino'
elif (sexo == 'F'):
    sex == 'Feminino'

while (sexo != 'M' and sexo != 'F'):
    sexo = str(input('sexo invalido: '))

esta_civil = str(input(
    'Qual seu Estado Civil: S para SOLTEIRO, C para CASADO, V para VIUVO ou D para DIVORCIADO: '))

esta_civil = esta_civil.upper()

if (esta_civil == 'S'):
    civil = 'Solteiro'
elif (esta_civil == 'C'):
    civil = 'Casado'
elif (esta_civil == 'V'):
    civil = 'Viúvo'
elif (esta_civil == 'D'):
    civil = 'Divorciado'

while (esta_civil != 'S') and (esta_civil != 'C') and (esta_civil != 'V') and (esta_civil != 'D'):
    esta_civil = str(input('Estado Civil invalido: '))


print('Todas informações preenchidas corretamente')
print(
    f'Sua idade: {idade}, seu Salario: {salario}, sexo: {sex} e seu Estado Civil: {civil}')
