nota1 = int(input('Inserir 1° nota do aluno: '))
nota2 = int(input('Inserir 2° nota do aluno: '))

nota_final = (nota1 + nota2) / 2

if (nota_final > 7.5):
    print(f'nota: {nota_final}, Conceito B')
if (nota_final > 9):
    print(
        f'nota: {nota_final}, Conceito A')
if (nota_final <= 7.4 and nota_final >= 6):
    print(f'nota: {nota_final}, Conceito C')
if (nota_final < 6 and nota_final > 4):
    print(f'nota: {nota_final}, Conceito D')
if (nota_final <= 4 and nota_final > 0):
    print(f'nota: {nota_final}, Conceito E')
