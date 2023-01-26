tamanho_arq = int(input('digite o tamanho do arquivo para download: '))
velocidade_inte = int(input('digite a velocidade da internet: '))


temp = tamanho_arq // velocidade_inte

print(
    f'Tempo que vai demorar para baixar esse arquivo com sua internet: {temp}')
