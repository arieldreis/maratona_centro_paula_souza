while True:
    partes = input().split()
    cor = partes[0]
    qtd_entregas = int(partes[1])
    capacidade = int(partes[2])

    if cor == "FIM":
        break
    consumos = input().split()
    energia = capacidade
    recargas = 0

    for i in range(qtd_entregas):
        consumo = int(consumos[i])
        if consumo > energia:
            recargas += 1
            energia = capacidade
        energia -= consumo
    print(cor, recargas, energia)
