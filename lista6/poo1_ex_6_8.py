entrada = input().split()
quantidade_irregulares, quantidade_palavras = [int(i) for i in entrada]

irregulares_singular = []
irregulares_plural = []
for i in range(0, quantidade_irregulares):
    entrada = input().split()
    irregulares_singular.append(entrada[0])
    irregulares_plural.append(entrada[1])

for i in range(0, quantidade_palavras):
    palavra = input()
    tamanho_palavra = len(palavra)
    if palavra in irregulares_singular:
        posicao = irregulares_singular.index(palavra)
        print(irregulares_plural[posicao])
    elif (palavra[tamanho_palavra-1] == 'y') and (palavra[tamanho_palavra-2] not in ['a', 'e', 'i', 'o', 'u']):
        print(palavra[:tamanho_palavra-1] + 'ies')
    elif (palavra[tamanho_palavra-1] in ['o', 's', 'x', 'o', 'u']) or \
            (palavra[tamanho_palavra-2:tamanho_palavra] in ['ch', 'sh']):
        print(palavra + 'es')
    else:
        print(palavra + 's')
