while True:
    try:
        entrada = input()

        hora = int(entrada[:2])
        hora = bin(hora)
        hora = hora[2:]
        while len(hora) != 4:
            hora = '0' + hora
        h = [' ', ' ', ' ', ' ']
        for i in range(0, 4):
            if hora[i] == '1':
                h[i] = 'o'

        minuto = int(entrada[3:5])
        minuto = bin(minuto)
        minuto = minuto[2:]
        while len(minuto) != 6:
            minuto = '0' + minuto
        m = [' ', ' ', ' ', ' ', ' ', ' ']
        for i in range(0, 6):
            if minuto[i] == '1':
                m[i] = 'o'

        print(' ____________________________________________')
        print('|                                            |')
        print('|    ____________________________________    |_')
        print('|   |                                    |   |_)')
        print('|   |   8         4         2         1  |   |')
        print('|   |                                    |   |')
        print(f'|   |   {h[0]}         {h[1]}         {h[2]}         {h[3]}  |   |')
        print('|   |                                    |   |')
        print('|   |                                    |   |')
        print(f'|   |   {m[0]}     {m[1]}     {m[2]}     {m[3]}     {m[4]}     {m[5]}  |   |')
        print('|   |                                    |   |')
        print('|   |   32    16    8     4     2     1  |   |_')
        print('|   |____________________________________|   |_)')
        print('|                                            |')
        print('|____________________________________________|')
        print()

    except EOFError:
        break
