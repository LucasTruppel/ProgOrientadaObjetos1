ordem = int(input())
P, Q, R, S, X, Y = [int(k) for k in input().split()]
i, j = [int(k) for k in input().split()]

Cij = 0
for k in range(1, ordem + 1):
    Aij = (P * i + Q * k) % X
    Bij = (R * k + S * j) % Y
    Cij += Aij * Bij

print(Cij)
