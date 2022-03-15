from math import ceil

print('-' * 70)
área = float(input('Qual o tamanho da área a ser pintada em m²? '))
print('-' * 70)
if área < 21.6 :
    print(f'Você pode comprar 1 galão de tinta de 18L que custará 80,00R$')
    print(f'ou 1 Lata de tinta de 3.6L que custará 25,00R$')
elif área > 21.6 or área > 108:
    Galão = ceil(área / 108 )
    Lata = ceil(área / 21.6)
    Comb1 = Galão - 1
    Sobra = ceil(área - (Comb1 * 108))
    Comb2 = ceil(Sobra / 21.6)
    print('-' * 70)
    print(f'Você usará {Galão} galões de tinta de 18L que custará R${Galão * 80},00 ')
    print(f'Ou usará {Lata} Latas de tinta de 3,6L que custará R${Lata * 25},00 ')
    if Comb1 > 0:
        print(f'Ou você pode levar {Comb1} Galão(ões) de 18L e mais {Comb2} Lata(s) de 3,6L. ')
    print(f'Por R${(Comb1 * 80) + (Comb2 * 25)},00 ')
    print('-' * 70)
