quantidade_senhas = int(input())
letras = ['GQaku', 'ISblv', 'EOYcmw', 'FPZdnx', 'JTeoy', 'DNXfpz', 'AKUgq', 'CMWhr', 'BLVis', 'HRjt']
for i in range(0, quantidade_senhas):
    frase = input()
    senha = ''
    tamanho_senha = 0
    for letra in frase:
        if letra == ' ':
            continue
        for j in range(0, 10):
            if letra in letras[j]:
                senha = senha + str(j)
                tamanho_senha = tamanho_senha + 1
                break
        if tamanho_senha == 12:
            break
    print(senha)
