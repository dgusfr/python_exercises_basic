valor_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

salario_bruto = valor_hora * horas_trabalhadas
ir = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
salario_liquido = salario_bruto - (ir + inss + sindicato)

print(f"+ Salário Bruto: R$ {salario_bruto}\n"
      f"- IR (11%): R$ {ir}\n"
      f"- INSS (8%): R$ {inss}\n"
      f"- Sindicato (5%): R$ {sindicato}\n"
      f"= Salário Líquido: R$ {salario_liquido}")
