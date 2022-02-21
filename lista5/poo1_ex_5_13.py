entrada = input().split()
altura_pulo, numero_canos = [int(i) for i in entrada]
entrada = input().split()
altura_canos = [int(i) for i in entrada]
resultado = 'YOU WIN'
for cano in range(0, numero_canos - 1):
    diferenca = altura_canos[cano + 1] - altura_canos[cano]
    if diferenca < 0:
        diferenca = -1 * diferenca
    if diferenca > altura_pulo:
        resultado = 'GAME OVER'
        break
print(resultado)
