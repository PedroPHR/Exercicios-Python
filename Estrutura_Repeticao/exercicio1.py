user = str(input('Digite seu nome de usuario: '))
senha = str(input('Digite sua senha: '))

while (user == senha):
    print('Senha invalida, a senha deve ser diferente do nome de usuario.')
    senha = str(input('Digite uma senha, observando os requisitos: '))
else:
    print('Senha valida.')
