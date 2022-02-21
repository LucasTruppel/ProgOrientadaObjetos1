quantidade_testes = int(input())
casa = 0
escritorio = 0
compra_casa = 0
compra_escritorio = 0
for i in range(0, quantidade_testes):
    ida, volta = input().split()
    if ida == 'chuva':
        if casa == 0:
            compra_casa = compra_casa + 1
            escritorio = escritorio + 1
        else:
            casa = casa - 1
            escritorio = escritorio + 1
    if volta == 'chuva':
        if escritorio == 0:
            compra_escritorio = compra_escritorio + 1
            casa = casa + 1
        else:
            escritorio = escritorio - 1
            casa = casa + 1
print(compra_casa, compra_escritorio)
