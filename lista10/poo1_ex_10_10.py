
# Dados do problema:
# Título: Etiquetas de Noel
# Origem: Por Neilor Tonin, URI Brasil
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/2482

quantidade_idiomas = int(input())
traducoes = {}
for i in range(0, quantidade_idiomas):
    idioma = input()
    frase = input()
    traducoes[idioma] = frase

quantidade_criancas = int(input())
for i in range(0, quantidade_criancas):
    nome = input()
    idioma = input()
    print(nome)
    print(traducoes[idioma])
    print()
