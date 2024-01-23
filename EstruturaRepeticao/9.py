limite = 500
a, b = 0, 1
serie_fibonacci = [a, b]

while b <= limite:
    a, b = b, a + b
    serie_fibonacci.append(b)

print(f"Série de Fibonacci até o valor maior que 500: {serie_fibonacci}")
