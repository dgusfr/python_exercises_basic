n = int(input("Digite quantos termos deseja na série de Fibonacci: "))

primeiro = 0
segundo = 1

serie_fibonacci = [primeiro, segundo]

while len(serie_fibonacci) < n:
    proximo = primeiro + segundo
    serie_fibonacci.append(proximo)
    primeiro = segundo
    segundo = proximo

print(f"Série de Fibonacci com {n} termos: {serie_fibonacci}")
