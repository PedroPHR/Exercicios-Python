print('PROGRAMA PARA CALCULAR TEMPO DE CRESCIMENTO DE UM PAIS PERANTE OUTRO')

paisA = float(input('Digite a população do Pais A: '))
paisB = float(input('Digite a população do Pais B: '))
cont = 0

while (paisA < paisB):
    crescimentoA = paisA * 0.03
    paisA += crescimentoA
    crescimentoB = paisB * 0.015
    paisB += crescimentoB
    cont += 1
    print(paisA, paisB)
else:
    print(
        f'Quantidade de anos que demorou para o Pais A passar em população do Pais B foi: {cont} Anos')
