# Dados do problema:
# Título: Conversão de Tempo
# Origem: Adaptado por Neilor Tonin, URI Brasil
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/1019

N = int(input())
horas = N // 3600
segundos = N - (horas * 3600)
minutos = segundos // 60
segundos = (segundos - (minutos * 60))
print('%d:%d:%d' % (horas, minutos, segundos))
