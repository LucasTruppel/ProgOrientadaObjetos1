quantidade_testes = int(input())
leds_por_numero = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
for i in range(0, quantidade_testes):
    quantidade_leds = 0
    numero = input()
    for j in range(0, len(numero)):
        quantidade_leds = quantidade_leds + leds_por_numero[int(numero[j])]
    print(f'{quantidade_leds} leds')
