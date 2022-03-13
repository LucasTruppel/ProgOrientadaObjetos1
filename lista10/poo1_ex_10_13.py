# Dados do problema:
# Título: A Sociedade do Anel
# Origem: Por Samuel Eduardo da Silva, IFSULDEMINAS/UFF Brazil
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/2949

quantidade_pessoas = int(input())
comitiva = {'X': 0, 'H': 0, 'E': 0, 'A': 0, 'M': 0}

for i in range(0, quantidade_pessoas):
    nome, tipo = input().split()
    comitiva[tipo] += 1

print(f"{comitiva['X']} Hobbit(s)")
print(f"{comitiva['H']} Humano(s)")
print(f"{comitiva['E']} Elfo(s)")
print(f"{comitiva['A']} Anao(s)")
print(f"{comitiva['M']} Mago(s)")
