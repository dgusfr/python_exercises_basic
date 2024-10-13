numero = int(input("Digite um número inteiro menor que 1000: "))

centenas = numero // 100 # 154 // 100 = 1
dezenas = (numero % 100) # 154 % 100  = 54 // 10 = 5
unidades = numero % 10   # 154 % 10 = 4 

if centenas > 0:
    print(f"{centenas} centenas, ")
else:
    print(f"{centenas} centena, ")

if dezenas > 0:
    print(f"{dezenas} dezenas,")
else:
    print(f"{dezenas} dezena,")

if unidades > 0:
    print(f"{unidades} unidades.")
else:
    print(f"{unidades} unidade.")
