salario_hora = float(input('Qual seu salario por hora: '))
horas_trabalhadas = float(input('Horario trabalhado no mês: '))

salario_mensal = salario_hora * horas_trabalhadas

ir = 0.0

if (salario_mensal > 900):
    ir = salario_mensal * 0.05
    percentual = 5
if (salario_mensal > 1500):
    ir = salario_mensal * 0.10
    percentual = 10
if (salario_mensal > 2500):
    ir = salario_mensal * 0.20
    percentual = 20
elif (salario_mensal <= 900):
    percentual = 0

fgts = salario_mensal * 0.11
inss = salario_mensal * 0.10

liquido = salario_mensal - inss - ir
total_desconto = inss + ir

print(
    f'Salário Bruto: ({salario_hora} * {horas_trabalhadas})             : R$ {salario_mensal}')
print(f'(-) IR ({percentual}%)                             : R$ {ir}')
print(f'(-) INSS (10%)                          : R$ {inss}')
print(f'FGTS (11%)                              : R$ {fgts}')
print(f'Total Descontos                         : R$ {total_desconto}')
print(f'Salário Liquido                         : R$ {liquido}')
