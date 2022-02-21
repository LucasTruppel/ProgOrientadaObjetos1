A, B = input().split()
A = int(A)
B = int(B)
if A == 0 or B == 0:
    print('Sao Multiplos')
elif A >= B:
    if A % B == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
else:
    if B % A == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
