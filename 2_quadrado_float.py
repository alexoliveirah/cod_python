while True:
    try:
        list1 = list()
        quad = list()
        for i in range(5):
            n = float(input(f"Informe o {i+1} número: "))
            list1.append(n)
            quad.append(list1[i] ** 2)
        print(f'Lista de números: {list1}')
        print(f'Lista com o valor quadrado dos números: {quad:}')
        resp = int(input('Deseja continuar?\nSim - 1\nNão - 2 '))
        if resp == 2:
            break
        elif resp != 1 and resp != 2:
            print('Número ou caractere inválido.')
    except:
        print('Número inválido!')
