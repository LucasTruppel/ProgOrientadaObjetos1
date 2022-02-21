notas = [50, 10, 5, 1]
n = 1
while True:
    valor = int(input())
    if valor == 0:
        break
    quantidade_nota = []
    for nota in notas:
        quantidade_nota.append(valor // nota)
        valor = valor % nota
    print('Teste', n)
    print(quantidade_nota[0], quantidade_nota[1], quantidade_nota[2], quantidade_nota[3])
    print()
    n = n + 1
