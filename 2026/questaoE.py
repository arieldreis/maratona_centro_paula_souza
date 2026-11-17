while True:
    entrada = input()

    if entrada == "ENCERRAR":
        break

    codigo, k = entrada.split()
    k = int(k)

    sinais = []

    while True:
        linha = input().split()

        if linha[0] == "FIM":
            break

        sinais.append(int(linha[1]))

    soma = sum(sinais[:k])
    maior = soma
    inicio = 1

    for i in range(k, len(sinais)):
        soma += sinais[i] - sinais[i-k]

        if soma > maior:
            maior = soma
            inicio = i - k + 2

    fim = inicio + k - 1

    print(codigo + ":", inicio, fim, maior)