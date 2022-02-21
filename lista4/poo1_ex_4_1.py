while True:
    entrada = input().split()
    X, Y = [int(i) for i in entrada]
    if X == 0 or Y == 0:
        break
    elif X > 0:
        if Y > 0:
            print('primeiro')
        else:
            print('quarto')
    else:
        if Y > 0:
            print('segundo')
        else:
            print('terceiro')
