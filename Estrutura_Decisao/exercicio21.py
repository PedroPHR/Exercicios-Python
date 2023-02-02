saque = int(input('Digite a quantia que deseja sacar: '))

sobras_deze50 = saque % 100
centenas = saque // 100
dezenas1 = sobras_deze50 // 50

saque2 = saque - 50
sobras_deze = saque2 % 100
dezenas = sobras_deze // 10

saque3 = saque2 - (dezenas * 10)
sobras_deze2 = saque3 % 100
dezenas2 = sobras_deze2 // 5

saque4 = saque - dezenas2
sobras_unid = saque4 % 10

print(saque4)
if (saque >= 10 and saque <= 600):
    print('Total de cedulas de dinheiro que vão ser disponibilizadas: ')
    print(f'saque: {saque} = {centenas} notas de 100, {dezenas1} notas de 50, {dezenas} notas de 10, {dezenas2} notas de 5 e {sobras_unid} notas de 1')
else:
    print('saque menor que 10 ou maior que 600')
