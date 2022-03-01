# Dados do problema:
# Título: Gasto de Combustível
# Origem: Adaptado por Neilor Tonin, URI Brasil
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/1017

horas = int(input())
velocidade = int(input())
litros_combustivel = (horas * velocidade) / 12
print('%.3f' % litros_combustivel)
