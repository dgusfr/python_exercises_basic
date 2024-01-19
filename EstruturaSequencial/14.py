peso = float(input("Digite o peso de peixes em quilos: "))
limite = 50
excesso = max(0, peso - limite)
multa = excesso * 4

print(f"Excesso de peso: {excesso} kg\nMulta a pagar: R$ {multa}")
