populacao_A = int(input("Informe a população do país A: "))
populacao_B = int(input("Informe a população do país B: "))
taxa_cresc_A = float(input("Informe a taxa de crescimento do país A (em decimal): "))
taxa_cresc_B = float(input("Informe a taxa de crescimento do país B (em decimal): "))

anos = 0
while populacao_A < populacao_B:
    populacao_A += populacao_A * taxa_cresc_A
    populacao_B += populacao_B * taxa_cresc_B
    anos += 1

print(f"São necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")

