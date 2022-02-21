quantidade_palavras = int(input())
for i in range(0, quantidade_palavras):
    palavra_codificada = input()
    palavra = []
    for j in range(0, len(palavra_codificada)):
        if palavra_codificada[j].islower():
            palavra.append(palavra_codificada[j])
    palavra.reverse()
    print(*palavra, sep='')
