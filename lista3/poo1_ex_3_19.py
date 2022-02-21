teste = 1
total_joao = 0
total_ze = 0
while True:
    quantidade_depositos = int(input())
    if quantidade_depositos == 0:
        break
    else:
        print('Teste %d' % teste)
        for deposito in range(1, quantidade_depositos + 1):
            entrada = input().split()
            deposito_joao, deposito_ze = [int(i) for i in entrada]
            total_joao = total_joao + deposito_joao
            total_ze = total_ze + deposito_ze
            diferenca = total_joao - total_ze
            print(diferenca)
        print()
        teste = teste + 1
        total_joao = 0
        total_ze = 0
