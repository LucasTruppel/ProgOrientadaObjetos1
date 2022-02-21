A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
if (abs(B-C) < A < B+C) and (abs(A-C) < B < A+C) and (abs(A-B) < C < A+B):
    perimetro = A + B + C
    print('Perimetro = %.1f' % perimetro)
else:
    area = (A + B) * C / 2
    print('Area = %.1f' % area)
