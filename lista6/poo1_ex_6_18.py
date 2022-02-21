while True:
    try:
        numero_linhas = int(input())
        frase = ''
        for i in range(0, numero_linhas):
            numero_bin = input()
            letra = chr(int(numero_bin, 2))
            frase = frase + letra
        print(frase)
    except EOFError:
        break
