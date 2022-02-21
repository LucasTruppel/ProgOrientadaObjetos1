quantidade_pessoas = int(input())
pesquisa = input().split()
favoraveis = pesquisa.count('0')
if favoraveis * 2 > quantidade_pessoas:
    print('Y')
else:
    print('N')
