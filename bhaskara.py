'''
Fórmula de Bhaskara
Coeficiente "a" não pode ser 0
Delta não pode ser negativo
'''

print(f"{'='*5}FÓRMULA DE BHASKARA{'='*5}")
a = float(input('Coeficiente a: '))
b = float(input('Coeficiente b: '))
c = float(input('Coeficiente c: '))

delta = b**2 - 4 * a * c
if a == 0 or delta < 0:
    print('Esta esquação não possui raizes reais.')
else:
    x1 = (-b + (delta ** (1/2))) / (2 * a)
    x2 = (-b - (delta ** (1/2))) / (2 * a)
    print(f'X1 = {x1:.4f}')
    print(f'X2 = {x2:.4f}')
