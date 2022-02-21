quantidade_letras = int(input())
palavra_hex = input().split()
palavra_dec = []
for letra_hex in palavra_hex:
    letra_dec = chr(int(letra_hex, 16))
    palavra_dec.append(letra_dec)
print(''.join(palavra_dec))
