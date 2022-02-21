while True:
    entrada = input().split()
    X1, Y1, X2, Y2 = [int(i) for i in entrada]
    if X1 == X2 == Y1 == Y1 == 0:
        break
    if X1 == X2 and Y1 == Y2:
        print('0')
    elif (abs(X2 - X1) == abs(Y2 - Y1)) or (X1 == X2) or (Y1 == Y2):
        print('1')
    else:
        print('2')
