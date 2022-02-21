while True:
    try:
        entrada = input().split()
        A, B, C = [int(i) for i in entrada]
        soma = A + B + C
        if soma == 1:
            if A == 1:
                print('A')
            elif B == 1:
                print('B')
            else:
                print('C')
        elif soma == 2:
            if A == 0:
                print('A')
            elif B == 0:
                print('B')
            else:
                print('C')
        else:
            print('*')
    except EOFError:
        break
