salario_colab = float(input('Digite seu salario: '))

aumento = 0.0
sal_aumento = 0.0
percentual = 0.0

if (salario_colab <= 280):
    aumento = salario_colab * 0.20
    sal_aumento = salario_colab + aumento
    percentual = 0.20
if (salario_colab > 280 and salario_colab <= 700):
    aumento = salario_colab * 0.15
    sal_aumento = salario_colab + aumento
    percentual = 0.15
if (salario_colab > 700 and salario_colab <= 1500):
    aumento = salario_colab * 0.10
    sal_aumento = salario_colab + aumento
    percentual = 0.10
if (salario_colab > 1500):
    aumento = salario_colab * 0.05
    sal_aumento = salario_colab + aumento
    percentual = 0.05

print(f'salario antes do reajuste: {salario_colab}')
print(
    f'Você recebeu um aumento de: {aumento}. Percentual de aumento: {percentual}. Salario atual: {sal_aumento}')
