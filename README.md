# Exercicios-Python

Esse repositório é destinado a exercicios de nivel facil em python, pois estou destinando meu tempo a aprender essa linguagem.
Conforme concluindo cada exercicio dou commit

round() = arredondar numeros. Exemplo: numero 1.50989 -- x = round(numero, -5) vai arredondar para baixo. já x = round(numero, +5) vai arredondar para cima.

upper() = Deixa a String em caixa alta. Exemplo: nome = 'pedro' -- x = nome.upper() - result = PEDRO

lower() = Deixa a String em caixa baixa. Exemplo: nome = 'PEDRO' -- x = nome.upper() - result = pedro

user = str(input('Digite seu nome de usuario: '))
senha = str(input('Digite sua senha: '))

while(user == senha):
	print('Senha invalida, a senha deve ser diferente do nome de usuario.')
	senha = str(input('Digite uma senha, observando os requisitos: '))
else: 
	print('Senha valida.')


nota = int(input('Digite uma nota: '))

while(nota > 10) or (nota < 0):
	print('Valor invalido, digite novamente')
	nota = int(input('Digite uma nota: '))
else:
	print('Valor Valido')


nome = 'Digite seu nome: '
quant = 0

for cara in nome:
	quant = quant + 1	

while (quant < 4):
	nome = str(input('Precisa conter mais de 3 digitos: '))

idade = int(input('digite sua idade: '))

while(idade < 0) or (idade > 150):
	idade = int(input('idade invalida: '))

salario = int(input('Digite seu salario: '))

while(salario < 0):

	salario = str(input('salario invalido: '))

sexo = str(input('qual seu sexo, Digite M para Masculino ou F para Feminino: '))

sexo = sexo.upper()

while(!'F'.equals(sexo)) or (!'M'.equals(sexo)):
	sexo = str(input('sexo invalido: '))

esta_civil = str(input('Qual seu Estado Civil: S para SOLTEIRO, C para CASADO, V para VIUVO ou D para DIVORCIADO: '))

esta_civil = esta_civil.upper()

while(esta_civil != 'S') or (esta_civil != 'C') or (esta_civil != 'V') or (esta_civil != 'D'):
	esta_civil = str(input('Estado Civil invalido: '))


print('Todas informações preenchidas corretamente')
