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
