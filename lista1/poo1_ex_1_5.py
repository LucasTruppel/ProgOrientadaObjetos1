# Dados do problema:
# Título: Salário com Bônus
# Origem: Adaptado por Neilor Tonin, URI Brasil
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/1009

nome = input()
salario = float(input())
vendas = float(input())
total = salario + vendas*0.15
print('TOTAL = R$ %.2f' % total)
