A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
if (abs(B-C) < A < B+C) and (abs(A-C) < B < A+C) and (abs(A-B) < C < A+B):
    if A == B == C:
        print('Valido-Equilatero')
    elif A == B or B == C or A == C:
        print('Valido-Isoceles')
    else:
        print('Valido-Escaleno')
    if A >= B and A >= C:
        if A*A == B*B + C*C:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
    elif B >= A and B >= C:
        if B*B == A*A + C*C:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
    else:
        if C*C == A*A + B*B:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
else:
    print('Invalido')
