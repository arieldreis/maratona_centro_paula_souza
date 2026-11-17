def buscar_rota(grafo, origem, destino):

    if origem == destino:
        return [origem]

    distancia = {}
    fila = [destino]

    distancia[destino] = 0
    inicio = 0

    # BFS
    while inicio < len(fila):
        atual = fila[inicio]
        inicio += 1

        for vizinho in grafo[atual]:
            if vizinho not in distancia:
                distancia[vizinho] = distancia[atual] + 1
                fila.append(vizinho)

    if origem not in distancia:
        return None

    # Montagem da rota
    rota = [origem]
    atual = origem

    while atual != destino:

        menor = None

        for vizinho in grafo[atual]:
            if vizinho in distancia:
                if distancia[vizinho] == distancia[atual] - 1:
                    if menor is None or vizinho < menor:
                        menor = vizinho

        atual = menor
        rota.append(atual)

    return rota


grafo = {}
identificador = ""

while True:

    linha = input().split()

    if linha[0] == "DESLIGAR":
        break

    elif linha[0] == "REDE":
        identificador = linha[1]
        grafo = {}

        print("DIAGNOSTICO", identificador)

    elif linha[0] == "LINK":

        a = linha[1]
        b = linha[2]

        if a not in grafo:
            grafo[a] = []

        if b not in grafo:
            grafo[b] = []

        grafo[a].append(b)
        grafo[b].append(a)

    elif linha[0] == "CONSULTAR":

        a = linha[1]
        b = linha[2]

        rota = buscar_rota(grafo, a, b)

        if rota is None:
            print(a, "=>", b, ": SEM ROTA")

        else:
            saltos = len(rota) - 1

            print(a, "=>", b, ":", saltos, "SALTOS")
            print("ROTA", *rota)

    elif linha[0] == "FECHAR":

        print("FIM", identificador)
        grafo = {}