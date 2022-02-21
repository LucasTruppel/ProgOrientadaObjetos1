import math
L, A, P, R = input().split()
L = int(L)
A = int(A)
P = int(P)
R = int(R)
menor_lado = L
diagonal = math.sqrt(L*L + A*A + P*P)
if R >= diagonal/2:
    print('S')
else:
    print('N')
