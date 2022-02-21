dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
entrada = input().split()
dia1, mes1 = [int(i) for i in entrada]
entrada = input().split()
dia2, mes2 = [int(j) for j in entrada]
if mes1 != mes2:
    dias_passados = dias_mes[mes1 - 1] - dia1
    for mes in range(mes1 + 1, mes2):
        dias_passados = dias_passados + dias_mes[mes - 1]
    dias_passados = dias_passados + dia2
else:
    dias_passados = dia2 - dia1
print(dias_passados)
