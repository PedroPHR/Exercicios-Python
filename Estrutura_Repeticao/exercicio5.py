print('PROGRAMA PARA CALCULAR TEMPO DE CRESCIMENTO DE UM PAIS PERANTE OUTRO')

paisA = float(input('Digite a população do Pais A: '))
paisB = float(input('Digite a população do Pais B: '))
taxaA = float(input('Digita a taxa de crescimento do pais A: '))
taxaB = float(input('Digita a taxa de crescimento do pais B: '))
cont = 0

if (paisA >= paisB):
    print('Impossivel fazer o calculo já que o pais A não deve ser mais que o pais B')
else:
    while (paisA < paisB):
        crescimentoA = paisA * taxaA
        paisA += crescimentoA
        crescimentoB = paisB * taxaB
        paisB += crescimentoB
        cont += 1
        # print(paisA, paisB)
    else:
        print(
            f'Quantidade de anos que demorou para o Pais A passar em população do Pais B foi: {cont} Anos')
