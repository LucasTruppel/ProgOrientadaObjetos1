while True:
    try:
        caracteres = " `1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./ "
        frase = input()
        frase_nova = ""
        for i in range(0, len(frase)):
            posicao = caracteres.find(frase[i])
            frase_nova = frase_nova + caracteres[posicao - 1]
        print(frase_nova)
    except EOFError:
        break
