valor = int(float(input())*100)
notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
    quantidade_nota = valor // (nota * 100)
    valor = valor % (nota * 100)
    print('%d nota(s) de R$ %.2f' % (quantidade_nota, nota))

print('MOEDAS:')
for moeda in moedas:
    quantidade_moeda = valor // (moeda * 100)
    valor = valor % (moeda * 100)
    print('%d moeda(s) de R$ %.2f' % (quantidade_moeda, moeda))
