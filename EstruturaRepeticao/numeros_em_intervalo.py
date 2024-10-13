inicio = int(input("Digite o número de início: "))
fim = int(input("Digite o número de fim: "))

# Garante que 'inicio' sempre seja o menor número e 'fim' o maior
if inicio > fim:
    # Se 'inicio' for maior que 'fim', trocamos os valores
    temp = inicio
    inicio = fim
    fim = temp

numeros_intervalo = list(range(inicio + 1, fim))

print(f"Números no intervalo: {numeros_intervalo}")
