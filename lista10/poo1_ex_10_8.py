# Dados do problema:
# Título: Roberto e a Sala Desenfreada
# Origem: Por José Wagner de Andrade Junior, Universidade Federal de Itajubá - UNIFEI Brazil
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/1953

while True:
    try:
        quantidade_alunos = int(input())
        alunos = {'EPR': 0, 'EHD': 0, 'INTRUSOS': 0}

        for i in range(0, quantidade_alunos):
            matricula, turma = input().split()
            if turma != 'EPR' and turma != 'EHD':
                alunos['INTRUSOS'] += 1
            else:
                alunos[turma] += 1

        print(f"EPR: {alunos['EPR']}")
        print(f"EHD: {alunos['EHD']}")
        print(f"INTRUSOS: {alunos['INTRUSOS']}")

    except EOFError:
        break
