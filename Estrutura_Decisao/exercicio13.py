semana = int(input('Digite um dia da semana: '))

dia_semana = ''

if (semana == 1):
    dia_semana = 'Domigo'

if (semana == 2):
    dia_semana = 'Segunda-Feira'

if (semana == 3):
    dia_semana = 'Terça-Feira'

if (semana == 4):
    dia_semana = 'Quarta-Feira'

if (semana == 5):
    dia_semana = 'Quinta-Feira'

if (semana == 6):
    dia_semana = 'Sexta-Feira'

if (semana == 7):
    dia_semana = 'Sabado'

else:
    dia_semana = 'Valor digitado não corresponde a um dia da semana'
print(f'Dia digitado: {semana}: dia que corresponde: {dia_semana}')
