def resolver(operacoes):
    operacoes.sort(key=lambda op: (op[2], op[1], op[0]))

    n = len(operacoes)

   
    anteriores = []

    for i in range(n):
        inicio = operacoes[i][1]
        p = -1

        for j in range(i - 1, -1, -1):
            if operacoes[j][2] <= inicio:
                p = j
                break

        anteriores.append(p)

   
    dp = [[0, 0, []]]

    for i in range(n):

        codigo = operacoes[i][0]
        pontuacao = operacoes[i][3]

        
        nao_selecionar = dp[i]

        
        estado_anterior = dp[anteriores[i] + 1]

        selecionar = [
            estado_anterior[0] + pontuacao,
            estado_anterior[1] + 1,
            estado_anterior[2] + [codigo]
        ]

       
        if selecionar[0] > nao_selecionar[0]:
            melhor = selecionar

        elif selecionar[0] < nao_selecionar[0]:
            melhor = nao_selecionar

        
        elif selecionar[1] < nao_selecionar[1]:
            melhor = selecionar

        elif selecionar[1] > nao_selecionar[1]:
            melhor = nao_selecionar

        
        else:
            if selecionar[2] < nao_selecionar[2]:
                melhor = selecionar
            else:
                melhor = nao_selecionar

        dp.append(melhor)

    return dp[n]



operacoes = [
    [1, 1, 3, 50],
    [2, 2, 5, 60],
    [3, 3, 6, 70],
    [4, 5, 7, 50],
    [5, 6, 8, 60],
    [6, 7, 9, 80]
]

resultado = resolver(operacoes)

print("Pontuação máxima:", resultado[0])
print("Quantidade de operações:", resultado[1])
print("Sequência de códigos:", resultado[2])