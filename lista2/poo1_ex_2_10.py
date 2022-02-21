N = int(input())
A, L, P = input().split()
A = int(A)
L = int(L)
P = int(P)
if A >= N and L >= N and P >= N:
    print('S')
else:
    print('N')
