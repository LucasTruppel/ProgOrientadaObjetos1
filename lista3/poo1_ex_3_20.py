copos_quedrados = 0
numero_bandejas = int(input())
for bandeja in range(1, numero_bandejas + 1):
    entrada = input().split()
    latas, copos = [int(i) for i in entrada]
    if latas > copos:
        copos_quedrados = copos_quedrados + copos
print(copos_quedrados)
