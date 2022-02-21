letra = input()
frase = input().split()
tamanho_frase = len(frase)
palavras = 0
for i in range(0, tamanho_frase):
    if letra in frase[i]:
        palavras = palavras + 1
porcentagem = palavras / tamanho_frase * 100
print(f'{porcentagem:.1f}')
