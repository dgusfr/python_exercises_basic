numeros = []  
n = int(input("Digite a quantidade de números que deseja inserir: "))

for i in range(n):
    numero = float(input(f"Digite o {i+1}º número: "))  
    numeros.append(numero)  

menor_valor = min(numeros)
maior_valor = max(numeros)
soma_valores = sum(numeros)

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Soma dos valores: {soma_valores}")
