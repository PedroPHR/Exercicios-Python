sexo = str(input('Digite seu sexo, sendo M -> Masculino e F -> Feminino: '))

sexo_convert = sexo.upper()

if (sexo_convert == 'F'):
    print('O sexo selecionado foi FEMININO')
elif (sexo_convert == 'M'):
    print('O sexo selecionado foi MASCULINO')
else:
    (f'Sexo Invalido, Caractere inserido: {sexo}')
