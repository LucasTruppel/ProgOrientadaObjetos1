# Dados do problema:
# Título: O Fantástico Jaspion
# Origem: Por Wanderley Guimarães, USP Brasil
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/1449

quantidade_instancias = int(input())
for i in range(0, quantidade_instancias):
    quantidade_palavras, quantidade_linhas = [int(k) for k in input().split()]
    dicionario = {}
    for j in range(0, quantidade_palavras):
        palavra_japones = input()
        traducao = input()
        dicionario[palavra_japones] = traducao

    for j in range(0, quantidade_linhas):
        palavras = input().split()
        linha_traduzida = ''
        for k in range(0, len(palavras)):
            if palavras[k] in dicionario:
                linha_traduzida += ' ' + dicionario[palavras[k]]
            else:
                linha_traduzida += ' ' + palavras[k]
        print(linha_traduzida.lstrip())
    print()
