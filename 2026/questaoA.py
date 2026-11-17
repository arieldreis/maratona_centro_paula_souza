while True:
    N, E = map(int, input().split())

    if N == 0 and E == 0:
        break

    consumos = list(map(int, input().split()))

    setores = 0

    for consumo in consumos:
        if E >= consumo:
            E -= consumo
            setores += 1
        else:
            break

    print(setores)