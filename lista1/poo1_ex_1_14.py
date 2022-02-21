A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

X, Y, Z = input().split()
X = int(X)
Y = int(Y)
Z = int(Z)

quantidade_largura = X // A
quantidade_comprimento = Y // B
quantidade_altura = Z // C
total = quantidade_largura * quantidade_comprimento * quantidade_altura
print(total)
