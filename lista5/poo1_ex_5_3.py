numero_elementos = int(input())
lista = input().split()
lista = [int(i) for i in lista]
minimo = min(lista)
posicao_minimo = lista.index(minimo)
print(f'Menor valor: {minimo}')
print(f'Posicao: {posicao_minimo}')
