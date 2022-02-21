dias_meses_anteriores = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
while True:
    try:
        entrada = input().split()
        mes, dia = [int(i) for i in entrada]
        dias_passados = dias_meses_anteriores[mes-1] + dia
        dias_natal = 360 - dias_passados
        if dias_natal > 1:
            print('Faltam %d dias para o natal!' % dias_natal)
        elif dias_natal == 1:
            print('E vespera de natal!')
        elif dias_natal == 0:
            print('E natal!')
        else:
            print('Ja passou!')
    except EOFError:
        break
