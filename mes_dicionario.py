meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
         9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}

while True:
    try:
        print(f"{'=' * 5} Quer ver os meses do ano? {'=' * 5}\n1 - Sim\n2 - Não")
        resp = int(input('Sua resposta: '))
        if resp == 2:
            print('Até a próxima!')
            break
        if resp != 1:
            print('Opção inválida! Tente novamente.')
            continue

        mes = int(input('Informe o número do mês que você quer ver: '))
        if mes > 12:
            print('Número inválido! Tente outro: ')
            continue
        print(f"{meses[mes]}")
    except:
        print('Caracter inválido! Tente novamente: ')
