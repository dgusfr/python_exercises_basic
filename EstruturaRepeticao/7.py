inicio = int(input("Digite o número de início: "))
fim = int(input("Digite o número de fim: "))

# Garante que o fim seja maior que o início
if inicio > fim:
    inicio, fim = fim, inicio

numeros_intervalo = list(range(inicio + 1, fim))

print(f"Números no intervalo: {numeros_intervalo}")
