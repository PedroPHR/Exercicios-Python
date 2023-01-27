import math

turno = str(
    input('Qual turno você estuda: M -> matutino, V -> vespertino, N -> noturno: '))

turn_mais = turno.upper()

if (turn_mais == 'M'):
    print('Seu turno é: Matutino')
if (turn_mais == 'V'):
    print('Seu turno é: Vespertino')
if (turn_mais == 'N'):
    print('Seu turno é: Noturno')
else:
    ('Turno não especificado')
