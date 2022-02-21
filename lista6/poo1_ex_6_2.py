while True:
    frase = input().split()
    if frase == ['*']:
        break
    palavra = frase[0]
    primeira_letra = palavra[0].lower()
    tautograma = 'Y'
    for i in range(1, len(frase)):
        palavra = frase[i]
        letra = palavra[0].lower()
        if primeira_letra != letra:
            tautograma = 'N'
            break
    print(tautograma)
