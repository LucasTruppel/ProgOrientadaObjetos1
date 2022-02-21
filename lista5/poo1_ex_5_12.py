entrada = input().split()
quantidade_torres, quantidade_picos = [int(i) for i in entrada]
entrada = input().split()
altura_torres = [int(j) for j in entrada]
tipo = 'beautiful'
contador_picos = 0
contador_vales = 0
picos = []
vales = []

for torre in range(1, quantidade_torres - 1):
    if altura_torres[torre] > altura_torres[torre - 1] and altura_torres[torre] > altura_torres[torre + 1]:
        picos.append(torre + 1)
        contador_picos = contador_picos + 1
    elif altura_torres[torre] < altura_torres[torre - 1] and altura_torres[torre] < altura_torres[torre + 1]:
        vales.append(torre + 1)
        contador_vales = contador_vales + 1

if (contador_picos != quantidade_picos) and (contador_vales != quantidade_picos - 1):
    tipo = 'ugly'
else:
    for i in range(1, picos[0] - 1):
        if altura_torres[i] > altura_torres[i + 1]:
            tipo = 'ugly'
            break
    for i in range(picos[-1] - 1, quantidade_torres - 1):
        if altura_torres[i] < altura_torres[i + 1]:
            tipo = 'ugly'
            break

print(tipo)
