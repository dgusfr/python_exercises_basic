numero = input("Digite um número inteiro positivo: ")
numero_invertido = ""

for i in range(len(numero) - 1, -1, -1):
    numero_invertido += numero[i]

numero_invertido = int(numero_invertido)
print(f"Invertido: {numero_invertido}")
