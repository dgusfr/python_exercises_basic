n = int(input("Digite o valor de N para a série: "))
soma_serie = 0
serie_termos = []

for i in range(1, n + 1):
    termo = i / (2 * i - 1)
    soma_serie += termo
    serie_termos.append(f"{i}/{2 * i - 1}")

print(f"Série até o {n}-ésimo termo: {' + '.join(serie_termos)}")
print(f"Soma da série: {soma_serie}")
