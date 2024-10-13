n = int(input("Digite o valor de N para a série de Fibonacci: "))
a, b = 0, 1
serie_fibonacci = [a, b]

while len(serie_fibonacci) < n:
    a, b = b, a + b
    serie_fibonacci.append(b)

print(f"Série de Fibonacci até o {n}-ésimo termo: {serie_fibonacci}")
