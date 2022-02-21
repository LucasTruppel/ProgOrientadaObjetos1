while True:
    digito, valor = input().split()
    if valor == '0' and digito == '0':
        break
    valor = '0' + valor
    valor = int(valor.replace(digito, ''))
    print(valor)
