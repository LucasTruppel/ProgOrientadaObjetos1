frase = input().split()
frase_nova = ''
for i in range(0, len(frase)):
    palavra = frase[i]
    palavra_nova = ''
    for j in range(1, len(palavra), 2):
        palavra_nova = palavra_nova + palavra[j]
    frase_nova = frase_nova + ' ' + palavra_nova
print(frase_nova.lstrip())
