N = int(input())
horas = N // 3600
segundos = N - (horas * 3600)
minutos = segundos // 60
segundos = (segundos - (minutos * 60))
print('%d:%d:%d' % (horas, minutos, segundos))
