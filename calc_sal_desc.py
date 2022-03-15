Salhora = float(input('Qual o seu salário por hora? '))
Quanthoras = int(input('Quantas horas trabalhadas no mês? '))
Sal = Salhora * Quanthoras
Ir = Sal * 11 /100
Inss = Sal * 8 / 100
Sindicato = Sal * 5 / 100
print(f'+ Seu salário bruto é de R${Sal}')
print(f'- IR (11%) : R${Ir}')
print(f'- INSS (8%) : R${Inss}')
print(f'- Sindicato (5%) : R${Sindicato}')
print('= Seu salário liquido é de R${:.2f}'.format(Sal - (Ir + Inss + Sindicato)))