populacao_A = 80000
populacao_B = 200000
taxa_cresc_A = 0.03
taxa_cresc_B = 0.015

anos = 0
while populacao_A < populacao_B:
    populacao_A += populacao_A * taxa_cresc_A
    populacao_B += populacao_B * taxa_cresc_B
    anos += 1

print(f"São necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")
