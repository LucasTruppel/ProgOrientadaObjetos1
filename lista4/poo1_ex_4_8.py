entrada = input().split()
largura_papel, altura_papel = [int(i) for i in entrada]
entrada = input().split()
largura_foto1, altura_foto1 = [int(j) for j in entrada]
entrada = input().split()
largura_foto2, altura_foto2 = [int(k) for k in entrada]

if (largura_foto1 + largura_foto2 <= largura_papel) and (altura_foto1 <= altura_papel) and (altura_foto2 <= altura_papel):
    print('S')
elif (largura_foto1 + largura_foto2 <= altura_papel) and (altura_foto1 <= largura_papel) and (altura_foto2 <= largura_papel):
    print('S')
elif (altura_foto1 + altura_foto2 <= largura_papel) and (largura_foto1 <= altura_papel) and (largura_foto2 <= altura_papel):
    print('S')
elif (altura_foto1 + altura_foto2 <= altura_papel) and (largura_foto1 <= largura_papel) and (largura_foto2 <= largura_papel):
    print('S')
elif (altura_foto1 + largura_foto2 <= largura_papel) and (largura_foto1 <= altura_papel) and (altura_foto2 <= altura_papel):
    print('S')
elif (altura_foto1 + largura_foto2 <= altura_papel) and (largura_foto1 <= largura_papel) and (altura_foto2 <= largura_papel):
    print('S')
elif (largura_foto1 + altura_foto2 <= largura_papel) and (altura_foto1 <= altura_papel) and (largura_foto2 <= altura_papel):
    print('S')
elif (largura_foto1 + altura_foto2 <= altura_papel) and (altura_foto1 <= largura_papel) and (largura_foto2 <= largura_papel):
    print('S')
else:
    print('N')
