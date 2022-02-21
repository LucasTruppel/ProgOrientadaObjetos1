quantidade_testes = int(input())
for i in range(0, quantidade_testes):
    entrada = input().split()
    palavra1, palavra2 = entrada
    tamanho_palavra1 = len(palavra1)
    tamanho_palavra2 = len(palavra2)
    nova_palavra = ''
    if tamanho_palavra1 > tamanho_palavra2:
        for j in range(0, tamanho_palavra2):
            nova_palavra = nova_palavra + palavra1[j] + palavra2[j]
        for k in range(tamanho_palavra2, tamanho_palavra1):
            nova_palavra = nova_palavra + palavra1[k]
    elif len(palavra1) < len(palavra2):
        for j in range(0, tamanho_palavra1):
            nova_palavra = nova_palavra + palavra1[j] + palavra2[j]
        for k in range(tamanho_palavra1, tamanho_palavra2):
            nova_palavra = nova_palavra + palavra2[k]
    else:
        for j in range(0, tamanho_palavra2):
            nova_palavra = nova_palavra + palavra1[j] + palavra2[j]
    print(nova_palavra)
