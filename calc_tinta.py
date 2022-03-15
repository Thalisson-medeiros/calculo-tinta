from math import ceil

área = float(input('Quantos m² tem a área a ser pintada? '))

if área <= 54 :
    print(f'A quantidade de tinta a ser comprada é de 1 galão')
    print('você pagará 80,00R$')
elif área > 54 :
    tinta = ceil(área / 54)
    print(f'A quantidade de tinta a ser comprada é de {tinta} galões')
    print(f'você pagará {tinta * 80}R$')