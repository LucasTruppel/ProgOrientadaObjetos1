entrada = int(input())
for numero in range(1, entrada + 1):
    if numero % 2 == 0:
        quadrado = numero * numero
        print('%d^2 = %d' % (numero, quadrado))
