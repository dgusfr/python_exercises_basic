numero = int(input("Digite um número inteiro menor que 1000: "))

centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = numero % 10

if centenas > 0:
    if centenas > 1:
        print(f"{centenas} centenas", end=", ")
    else:
        print(f"{centenas} centena", end=", ")

if dezenas > 0:
    if dezenas > 1:
        print(f"{dezenas} dezenas", end=" e ")
    else:
        print(f"{dezenas} dezena", end=" e ")

if unidades > 0:
    if unidades > 1:
        print(f"{unidades} unidades")
    else:
        print(f"{unidades} unidade")
