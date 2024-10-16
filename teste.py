"""aluno = {
  "nome": {
      "nota1" : "nota" 
      "nota2" : "nota" 
      "nota3" : "nota" 
  }
}"""
alunos = []

def adicionar_alunos():
  cond = True
  while cond:
    nome = input("Nome do aluno:")
    nota1 = float(input("Digite a primeira nota"))
    nota2 = float(input("Digite a primeira nota"))
    nota3 = float(input("Digite a primeira nota"))

    alunos[nome] = {'nota1': nota1, 'nota2': nota2, 'nota3': nota3}

def imprime_boletim_turma():
    if not alunos:
        print("O Boletim está vazio.")
        return
    
    print("\Boletim da Turma:")
    for nome, dados in alunos.items():
          print(f"{nome} \n - 1ª Nota: {dados['nota1']:.2f} - 2ª Nota: {dados['nota2']} - 3ª Nota: {dados['nota3']}")
    print()

def calcular_media():



# def classifica_aluno():




def sistema_de_notas():
        print("\n=== Sistema de Notas ===")
        print("1. Adicionar Aluno")
        print("2. Média das notas")
        print("3. Ranking")
        print("5. Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um número inteiro.")

        match opcao:
            case 1:
                adicionar_alunos()
            case 2:
                calcular_media()
            case 3:
                classifica_aluno()
            case 4:
                imprime_boletim_classe()
            case 5:
                print("Saindo do sistema...")
            case _:
                print("Opção inválida, tente novamente.")
    
sistema_de_notas()
