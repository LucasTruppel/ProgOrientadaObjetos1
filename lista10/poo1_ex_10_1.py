# Dados do problema:
# Título: Pontos de Feno
# Origem: Por Gordon V. Cormack Canadá
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/1261

palavras = {}
quantidade_palavras, quantidade_descricoes = [int(k) for k in input().split()]
for i in range(0, quantidade_palavras):
    palavra, valor = input().split()
    palavras[palavra] = int(valor)

for i in range(0, quantidade_descricoes):
    salario = 0
    while True:
        linha = input().split()
        if linha == ['.']:
            break
        for palavra in linha:
            if palavra in palavras:
                salario += palavras[palavra]
    print(salario)
