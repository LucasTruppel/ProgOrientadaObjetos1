# Dados do problema:
# Título: Ida à Feira
# Origem: Por Neilor Tonin, URI Brasil
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/1281

quantidade_idas = int(input())
for i in range(0, quantidade_idas):
    quantidade_produtos = int(input())
    produtos = {}
    for j in range(0, quantidade_produtos):
        produto, preco = input().split()
        produtos[produto] = float(preco)

    quantidade_compras = int(input())
    valor = 0
    for j in range(0, quantidade_compras):
        produto, quantidade = input().split()
        valor += produtos[produto] * int(quantidade)
    print(f'R$ {valor:.2f}')
