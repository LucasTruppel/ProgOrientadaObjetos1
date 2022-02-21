numero_pessoas = int(input())
instante_deteccao = int(input())
tempo_acumulado = 10
instante_desligamento_anterior = instante_deteccao + 10
for pessoa in range(2, numero_pessoas + 1):
    instante_deteccao = int(input())
    instante_desligamento = instante_deteccao + 10
    if instante_desligamento_anterior + 10 <= instante_desligamento:
        tempo_acumulado = tempo_acumulado + 10
    else:
        tempo_acumulado = tempo_acumulado + instante_desligamento - instante_desligamento_anterior
    instante_desligamento_anterior = instante_desligamento
print(tempo_acumulado)
