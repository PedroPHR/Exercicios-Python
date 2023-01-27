n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))
print(n1, n2, n3)
maior = n1
menor = n1

if (n3 > n2):
    temp = n3
    n3 = n2
    n2 = temp

if (n2 > n1):
    temp = n2
    n2 = n1
    n1 = temp

if (n3 > n2):
    temp = n3
    n3 = n2
    n2 = temp


print(n1, n2, n3)
