turno = input("Em que turno você estuda? (M-matutino, V-Vespertino, N-Noturno): ")

if turno.upper() == "M":
    print("Bom Dia!")
elif turno.upper() == "V":
    print("Boa Tarde!")
elif turno.upper() == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
