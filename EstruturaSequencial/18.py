tamanho_arquivo = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_internet = float(input("Digite a velocidade do link de Internet (em Mbps): "))

tempo_download_minutos = (tamanho_arquivo / velocidade_internet) * 60

print(f"O tempo aproximado de download é de {tempo_download_minutos:.2f} minutos")
