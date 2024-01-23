n = int(input("Digite a quantidade de números: "))
numeros = [float(input(f"Digite o {i+1}º número: ")) for i in range(n)]

menor_valor = min(numeros)
maior_valor = max(numeros)
soma_valores = sum(numeros)

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Soma dos valores: {soma_valores}")
