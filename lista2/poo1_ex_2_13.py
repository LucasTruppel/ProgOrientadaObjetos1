A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
H, L = input().split()
H = int(H)
L = int(L)
if (H >= A and L >= B) or (H >= B and L >= A):
    print('S')
elif (H >= A and L >= C) or (H >= C and L >= A):
    print('S')
elif (H >= B and L >= C) or (H >= C and L >= B):
    print('S')
else:
    print('N')
