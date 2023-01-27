salario_hora = int(input('Qual seu salario por hora: '))
horas_trabalhadas = int(input('Horario trabalhado no mês: '))

salario_mensal = salario_hora * horas_trabalhadas

inss = salario_mensal * 0.08

imposto_renda = salario_mensal * 0.11

sindicato = salario_mensal * 0.05

salario_liquido = salario_mensal - inss - sindicato - imposto_renda
print(f'Salario Bruto: {salario_mensal}')
print(f'Desconto INSS: {inss}')
print(f'Desconto IMPOSTO DE RENDA: {imposto_renda}')
print(f'Desconto SINDICATO: {sindicato}')
print(f'Salario Liquido: {salario_liquido}')
