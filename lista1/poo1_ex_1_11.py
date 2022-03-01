# Dados do problema:
# Título: Idade em Dias
# Origem: Adaptado por Neilor Tonin, URI Brasil
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/1020

dias = int(input())
anos = dias // 365
dias = dias - (anos * 365)
meses = dias // 30
dias = dias - (meses * 30)
print('%d ano(s)' % anos)
print('%d mes(es)' % meses)
print('%d dia(s)' % dias)
