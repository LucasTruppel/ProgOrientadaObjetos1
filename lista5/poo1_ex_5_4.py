while True:
    entrada = input()
    if entrada == '0 0':
        break
    bilhetes_coletados = input().split()
    bilhetes_unicos = list(set(bilhetes_coletados))
    bilhetes_repetidos = 0
    for bilhete in bilhetes_unicos:
        quantidade_bilhete = bilhetes_coletados.count(bilhete)
        if quantidade_bilhete > 1:
            bilhetes_repetidos = bilhetes_repetidos + 1
    print(bilhetes_repetidos)
