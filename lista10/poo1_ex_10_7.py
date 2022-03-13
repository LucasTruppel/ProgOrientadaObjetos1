# Dados do problema:
# Título: Ajude Girafales
# Origem: Por Dâmi Henrique, Inatel Brazil
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/1911

while True:
    tamanho_turma = int(input())
    if tamanho_turma == 0:
        break
    assinaturas = {}
    for i in range(0, tamanho_turma):
        aluno, assinatura_original = input().split()
        assinaturas[aluno] = assinatura_original

    quantidade_falsas = 0
    quantidade_alunos = int(input())
    for i in range(0, quantidade_alunos):
        aluno, assinatura = input().split()
        diferencas = 0
        assinatura = list(assinatura)
        assinatura_original = list(assinaturas[aluno])
        for j in range(0, len(assinatura)):
            if assinatura[j] != assinatura_original[j]:
                diferencas += 1
        if diferencas > 1:
            quantidade_falsas += 1
    print(quantidade_falsas)
