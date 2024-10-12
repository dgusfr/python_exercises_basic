salario = float(input("Digite o salário do colaborador: "))

if salario <= 1500:
    percentual = 20
elif salario <= 2000:
    percentual = 15
elif salario <= 3000:
    percentual = 10
else:
    percentual = 5

aumento = (salario * percentual) / 100
novo_salario = salario + aumento

print(f"Salário antes do reajuste: R${salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R${aumento:.2f}")
print(f"Novo salário após o aumento: R${novo_salario:.2f}")
