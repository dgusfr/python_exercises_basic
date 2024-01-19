area_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros_necessarios = area_pintada / 3
latas_necessarias = litros_necessarios / 18
preco_total = latas_necessarias * 80

print(f"Quantidade de latas necessárias: {latas_necessarias:.2f}\nPreço total: R$ {preco_total:.2f}")
