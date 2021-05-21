"""
Ler uma matriz 4 x 4, conte e escreva quantos valores são maiores que 10.
"""

matriz = list()
maior = list()
print(f"{'=' * 5}Matriz 4 x 4{'=' * 5}\n")

for i in range(4):  # For para repetir 4x, tendo o total das quatro séries desejadas
    print(f'{i + 1}ª Série')
    n1 = int(input(f'1º número: '))
    n2 = int(input(f'2º número: '))
    n3 = int(input(f'3º número: '))
    n4 = int(input(f'4º número: '))
    matriz.extend([[n1, n2, n3, n4]])  # Extend usa colchetes por padrão [] mas para adicionar o quatro números como
    # uma lista foi necessário mais um par de colchetes para q fosse interpretado como uma única lista.

for i in matriz:
    for j in i:  # i é as listas dentro da lista matriz e j são os elementos dentro delas
        if j > 10:
            maior.append(j)

print(f'Temos um total de {len(maior)} números maiores que 10.')
print(f'Lista com os números = {maior}')
