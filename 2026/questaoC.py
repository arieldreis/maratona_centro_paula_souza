maior = -1
menor = 201

while True:
    entrada = input().split()
    n = int(entrada[0])
    l = int(entrada[1])

    if n == 0 and l == 0:
        break

    temp = list(map(int, input().split()))

    total = 0
    seq = 0
    maior_seq = 0

    for t in temp:
        if t > l:
            total += 1
            seq += 1

            if seq > maior_seq:
                maior_seq = seq
        else:
            seq = 0

        if t > maior:
            maior = t

        if t < menor:
            menor = t

    print(total, maior_seq)

print(">T", maior)
print("<T", menor)