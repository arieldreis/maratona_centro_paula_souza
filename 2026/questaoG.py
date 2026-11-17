while True:
    linha = input().split()

    if linha[0] == "ENCERRAR":
        break

    id_robo = linha[1]
    capacidade = int(linha[3])

    codigos = []
    pesos = []

    while True:
        linha = input().split()

        if linha[0] == "DESPACHAR":
            break

        codigos.append(linha[1])
        pesos.append(int(linha[2]))

    qtd = len(codigos)

    pesados = sorted(range(qtd), key=lambda i: (-pesos[i], codigos[i]))
    leves = sorted(range(qtd), key=lambda i: (pesos[i], codigos[i]))

    usado = [False] * qtd
    pos_pesado = 0
    pos_leve = 0
    restantes = qtd
    viagens = []

    while restantes > 0:
        while usado[pesados[pos_pesado]]:
            pos_pesado = pos_pesado + 1
        pesado = pesados[pos_pesado]
        usado[pesado] = True
        restantes = restantes - 1

        while pos_leve < qtd and usado[leves[pos_leve]]:
            pos_leve = pos_leve + 1

        if pos_leve < qtd:
            leve = leves[pos_leve]

            if pesos[pesado] + pesos[leve] <= capacidade:
                usado[leve] = True
                restantes = restantes - 1
                viagens.append(codigos[pesado] + " " + codigos[leve])
            else:
                viagens.append(codigos[pesado])
        else:
            viagens.append(codigos[pesado])

    print(id_robo, "VIAGENS", len(viagens))
    for numero in range(len(viagens)):
        print(numero + 1, viagens[numero])