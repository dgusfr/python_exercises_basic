numero = int(input("Fatorial de: "))
fatorial = 1

print(f"{numero}! =", end=" ")
for i in range(1, numero + 1):
    fatorial *= i
    if i < numero:
        print(f"{i} .", end=" ")
    else:
        print(f"{i} =", end=" ")

print(fatorial)
