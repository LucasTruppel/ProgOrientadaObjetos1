testes = int(input())
for teste in range(1, testes + 1):
    entrada = input().split()
    X1, Y1, X2, Y2, X3, Y3 = [int(i) for i in entrada]
    area = (X1*(Y2-Y3) - Y1*(X2-X3) + X2*Y3 - X3*Y2) / 2
    if area < 0:
        area = area * -1
    print('%.3f' % area)
