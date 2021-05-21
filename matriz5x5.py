"""
Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0  os demais elementos.
Escreva ao final a matriz obtida
"""


matriz = list()

# Para uma matriz 5 x 5 coloquei um range de 5 em ambos for porque serão cinco linhas e cinco colunas.
for i in range(5):
    numbers = list()  # Lista para guardar todos os números gerados no segundo for e posteriomente ser adicionado como
    # uma única lista ao invés de diversas listas.
    a, b = 0, 1
    for j in range(5):
        if j == i:  # A váriavel b = 1 será adicionada na posição correspondente ao valor da váriavel i no primeiro for.
            numbers.append(b)
        else:
            numbers.append(a)
    matriz.extend([numbers])  # Usei o extend para adicionar os valores contidos em numbers como uma lista única.

for i in matriz:
    print(i)
