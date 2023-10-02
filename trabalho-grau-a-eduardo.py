capacidade_volume = 0
capacidade_peso = 0
peso_carregado = 0
volume_carregado = 0
pacotes = []

def menu():
    print("\n..:: MENU ::..\n")
    print("1 - Iniciar dia")
    print('2 - Realizar parada')
    print("3 - Consultar situação")
    print("4 - Listar pacotes")
    print("5 - Finalizar dia")
    print("6 - Gerar relatório")
    print("7 - Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

def realizar_parada(pacotes, capacidade_peso, capacidade_volume, peso_carregado, volume_carregado):
    while True:
        print("\n..:: MENU DA PARADA ::..\n")
        print("1 - Inserir pacote")
        print("2 - Retirar pacote")
        print("3 - Encerrar parada")
        escolha_parada = input("Escolha uma opção: ")
        
        if escolha_parada == "1":
            peso_pacote = int(input("Informe o peso do pacote (1-99 kg): "))
            valor_mercadoria = float(input("Informe o valor da mercadoria: "))
            
            custo_transporte = peso_pacote * 1.50
            seguro_peso_max = capacidade_volume * 10

            if peso_pacote > seguro_peso_max:
                adicional_seguro = (peso_pacote - seguro_peso_max) * 0.80
                resposta_seguro = input("Seguro excedente: R$ ", adicional_seguro, ". Aceita? (S/N): ")
                if resposta_seguro.upper() != 'S':
                    print("Pacote não aceito.")
                    continue
            
            if peso_carregado + peso_pacote <= capacidade_peso and volume_carregado + 1 <= capacidade_volume:
                pacotes.append((peso_pacote, valor_mercadoria))
                peso_carregado += peso_pacote
                volume_carregado += 1
                print("Pacote aceito. Custo de transporte: R$ ", custo_transporte)
            else:
                print("Pacote não aceito. Capacidade excedida.")
                
        
        elif escolha_parada == "2":
            if pacotes:
                ultimo_pacote = pacotes.pop()
                peso_pacote, _ = ultimo_pacote
                peso_carregado -= peso_pacote
                volume_carregado -= 1
                print("Pacote retirado. Peso: ", peso_pacote, " kg")
            else:
                print("Não há pacotes para retirar.")
        
        elif escolha_parada == "3":
            print("Parada encerrada.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def consultar_situacao(capacidade_peso, peso_carregado, capacidade_volume, volume_carregado):
    print("\nSituação do Caminhão:")
    print("Peso carregado: ", peso_carregado, " kg")
    print("Peso restante: ", capacidade_peso - peso_carregado, " kg")
    print("Peso máximo: ",capacidade_peso , " kg")
    print("Volume carregado: ", volume_carregado, " m³")
    print("Volume restante: ", capacidade_volume - volume_carregado, " m³")
    print("Volume máximo: ", capacidade_volume, " m³")

def listar_pacotes(pacotes):
    print("\nPacotes no Caminhão:")
    for i, pacote in enumerate(pacotes):
        peso, _ = pacote
        print("Pacote ", i + 1, ": Peso", peso, " kg")

def gerar_relatorio(pacotes):
    if not pacotes:
        print("Não há pacotes para gerar relatório.")
        return
    
    menor_peso = min(p[0] for p in pacotes)
    maior_peso = max(p[0] for p in pacotes)
    menor_quantidade = min(len(pacotes), key=lambda x: len(x))
    maior_quantidade = max(len(pacotes), key=lambda x: len(x))
    menor_peso_total = min(sum(p[0] for p in pacotes))
    maior_peso_total = max(sum(p[0] for p in pacotes))
    
    print("\n..:: RELATÓRIO DO DIA ::..\n")
    print("Menor peso de pacote individual transportado: ", menor_peso, " kg")
    print("Maior peso de pacote individual transportado: ", maior_peso, " kg")
    print("Menor quantidade de pacotes embarcados em uma parada: ", menor_quantidade)
    print("Maior quantidade de pacotes embarcados em uma parada: ", maior_quantidade)
    print("Menor quantidade total de peso no caminhão ao encerrar parada: ", menor_peso_total, " Kg")
    print("Maior quantidade total de peso no caminhão ao encerrar parada: ", maior_peso_total, " Kg")

while True:
    escolha = menu()
    if escolha == "1":
        capacidade_volume = int(input("Informe a capacidade máxima de volume em m³: "))
        capacidade_peso = int(input("Informe o peso máximo de carga total em kg: "))
        peso_carregado = 0
        volume_carregado = 0
        pacotes = []
        print("Dia iniciado.")
        
    elif escolha == "2":
        if capacidade_volume == 0:
            print("Erro: Dia não iniciado. Primeiro, inicie o dia.")
        else:
            realizar_parada(pacotes, capacidade_peso, capacidade_volume, peso_carregado, volume_carregado)
        
    elif escolha == "3":
        consultar_situacao(capacidade_peso, peso_carregado, capacidade_volume, volume_carregado)
        
    elif escolha == "4":
        listar_pacotes(pacotes)
        
    elif escolha == "5":
        print("Dia finalizado.")
        
    elif escolha == "6":
        gerar_relatorio(pacotes)
        
    elif escolha == "7":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")