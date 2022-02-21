while True:
    tipos_varetas = int(input())
    if tipos_varetas == 0:
        break
    duplas_varetas = 0
    for tipo in range(0, tipos_varetas):
        entrada = input().split()
        quantidade_varetas = int(entrada[1])
        duplas_varetas = duplas_varetas + quantidade_varetas // 2
    quantidade_retangulos = duplas_varetas // 2
    print(quantidade_retangulos)
