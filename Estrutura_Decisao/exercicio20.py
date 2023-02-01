nota1 = int(input('Inserir 1° nota do aluno: '))
nota2 = int(input('Inserir 2° nota do aluno: '))
nota3 = int(input('Inserir 3° nota do aluno: '))

nota_final = (nota1 + nota2 + nota3) / 3

if (nota_final >= 7 and nota_final <= 9):
    print(f'Parabéns Você foi aprovado, nota: {nota_final}')
elif (nota_final < 7):
    print(f'Você foi reprovado, nota: {nota_final}')
elif (nota_final == 10):
    print(f'Parabéns Você foi aprovado com distinção, nota: {nota_final}')
