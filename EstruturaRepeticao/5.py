numeros = [float(input(f"Digite o {i+1}º número: ")) for i in range(5)]
soma = sum(numeros)
media = soma / len(numeros)

print(f"Soma dos números: {soma}")
print(f"Média dos números: {media}")
