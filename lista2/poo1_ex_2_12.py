A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
primeiro = A
if B < A < C or C < A < B:
    print(A)
elif A < B < C or C < B < A:
    print(B)
else:
    print(C)
