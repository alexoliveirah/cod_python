"""Sequência de Fibonacci
os números seguintes serão a soma dos dois números anteriores
ex: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584..."""

try:
    term = int(input('Quantos termos você quer ver? '))
    t1 = 0
    t2 = 1
    t3 = 0
    print(f'{t1} - {t2}', end=' ')
    for i in range(term - 2):
        t3 = t1 + t2
        print(f'- {t3}', end=' ')
        t1 = t2
        t2 = t3
except:
    print('Digite um número inteiro e positivo.')