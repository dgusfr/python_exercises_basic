n = int(input("Digite o valor de N para a série: "))
soma_serie = 0

for i in range(1, n + 1):
    soma_serie += i / (2 * i - 1)

print(f"Série até o {n}-ésimo termo: {soma_serie}")
