entrada = input().split()
tempos = [float(i) for i in entrada]
competidores = ['Otavio', 'Bruno', 'Ian']
menor_tempo = min(tempos)
posicao = tempos.index(menor_tempo)
quantidade = tempos.count(menor_tempo)
if quantidade != 1:
    print('Empate')
else:
    print(competidores[posicao])
