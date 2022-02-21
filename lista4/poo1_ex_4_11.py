while True:
    try:
        entrada = input().split()
        angulo_horas, angulo_minutos = [int(i) for i in entrada]
        horas = angulo_horas // 30
        minutos = angulo_minutos // 6
        if horas < 10:
            if minutos == 0:
                print('0%d:00' % horas)
            elif minutos < 10:
                print('0%d:0%d' % (horas, minutos))
            else:
                print('0%d:%d' % (horas, minutos))
        else:
            if minutos == 0:
                print('%d:00' % horas)
            elif minutos < 10:
                print('%d:0%d' % (horas, minutos))
            else:
                print('%d:%d' % (horas, minutos))
    except EOFError:
        break
