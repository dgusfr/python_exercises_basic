num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

resultado = 0.0

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 / num2

classificacao = ""
if resultado % 2 == 0:
    classificacao += "O numero é par "
else:
    classificacao += "O numero é par ímpar "

if resultado >= 0:
    classificacao += "positivo "
else:
    classificacao += "negativo "

if resultado.is_integer():
    classificacao += "inteiro"
else:
    classificacao += "decimal"

print(f"Resultado: {resultado}")
print(f"Classificação: {classificacao}")
