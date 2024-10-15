"""
INICIO
LER N
Para cada i de 2 ate N faça:
    p = true
    Se N% i == 0:
        "Numero não é primo"
        p == false
    Caso contrario:
        "Numero é primo"

FIM

Note que se desejarmos determinar se um numero muito grande como 1.256.876 é primo a complexidade do algoritmo aumenta muit.
Para melhorar isso usamos o loop até a raiz quadrada do numeor em questão.
"""

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite um número inteiro: "))

if eh_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
