
def setEstacoes(estacoes):
    resultado = []

    for i in range(estacoes):
        dados = input().split()

        letra = dados[0]
        energia = int(dados[1])
        quantidade = int(dados[2])
        atendidos = 0

        for j in range(quantidade):
            solicitacao = int(dados[j + 3])

            if energia >= solicitacao:
                energia -= solicitacao
                atendidos += 1

        resultado.append([letra, atendidos, energia])

    resultado.sort(key=lambda x: (-x[2], x[0]))

    for estacao in resultado:
        print(*estacao)


while True:
    estacoes = int(input())

    if estacoes == 0:
        break

    setEstacoes(estacoes)
