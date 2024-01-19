area_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros_necessarios = area_pintada / 6

latas_necessarias = litros_necessarios / 18
preco_latas = latas_necessarias * 80

galoes_necessarios = litros_necessarios / 3.6
preco_galoes = galoes_necessarios * 25

mistura_latas = int(latas_necessarias)
mistura_galoes = round((litros_necessarios % 18) / 3.6)

preco_mistura = (mistura_latas * 80) + (mistura_galoes * 25)

print(f"Comprando apenas latas de 18 litros:\nQuantidade de latas necessárias: {latas_necessarias:.2f}\nPreço")
