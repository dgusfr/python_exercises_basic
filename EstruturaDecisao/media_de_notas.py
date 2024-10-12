nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 2

if media == 10:
    print("Aluno Aprovado com Distinção")
elif media >= 7:
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado")

print(f"A média para ser aprovado é 7")
