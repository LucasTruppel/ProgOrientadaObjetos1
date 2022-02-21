codigo, quantidade = input().split()
codigo = int(codigo)
quantidade = int(quantidade)
if codigo == 1:
    valor = 4 * quantidade
elif codigo == 2:
    valor = 4.5 * quantidade
elif codigo == 3:
    valor = 5 * quantidade
elif codigo == 4:
    valor = 2 * quantidade
else:
    valor = 1.5 * quantidade
print('Total: R$ %.2f' % valor)
