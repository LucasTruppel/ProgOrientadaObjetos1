while True:
    try:
        entrada = input().split()
        voluntarios_foram, voluntarios_voltaram = [int(i) for i in entrada]
        indentificadores_registrados = input().split()
        if voluntarios_foram == voluntarios_voltaram:
            print('*')
        else:
            indentificadores_registrados = [int(j) for j in indentificadores_registrados]
            indentificadores_perdidos = list(range(1, voluntarios_foram + 1))
            for indentificador in indentificadores_registrados:
                indentificadores_perdidos.remove(indentificador)
            print(' '.join(map(str, indentificadores_perdidos))+' ')
    except EOFError:
        break
