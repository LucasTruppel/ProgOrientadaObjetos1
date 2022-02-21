while True:
    quantidade_suspeitos = int(input())
    if quantidade_suspeitos == 0:
        break
    entrada = input().split()
    suspeitos = [int(i) for i in entrada]
    suspeitos_original = suspeitos.copy()
    mais_suspeito = max(suspeitos)
    suspeitos.remove(mais_suspeito)
    assassino = suspeitos_original.index(max(suspeitos)) + 1
    print(assassino)
