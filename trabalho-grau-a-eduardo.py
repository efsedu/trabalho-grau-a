capacidade_volume = 0
capacidade_peso = 0
peso_carregado = 0
volume_carregado = 0
menor_quantidade_por_parada = None
maior_quantidade_por_parada = 0
menor_peso_caminhao_por_parada = None
maior_peso_caminhao_por_parada = 0
maior_peso_excedente = 0
maior_valor_excedente = 0
valor_total_transportado = 0
valor_total_excedente = 0
seguro_peso_max = 0
pacotes = []

#Menu principal
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

def realizar_parada():
    global capacidade_peso, peso_carregado, volume_carregado, capacidade_volume, pacotes, menor_quantidade_por_parada, maior_quantidade_por_parada, maior_peso_caminhao_por_parada, menor_peso_caminhao_por_parada, maior_valor_excedente, maior_peso_excedente, valor_total_transportado, valor_total_excedente, seguro_peso_max
    pacotes_carregados = 0
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

            #verifica se o pacote necessita de seguro extra
            peso_a_ser_carregado = peso_carregado + peso_pacote
            adicional_peso = 0
            adicional_seguro = 0
            if peso_a_ser_carregado > seguro_peso_max:
                adicional_peso =  peso_a_ser_carregado - seguro_peso_max
                adicional_seguro = adicional_peso * 0.80
                resposta_seguro = input("Seguro excedente: R$ {:.2f}. Aceita? (S/N): ".format(adicional_seguro))
                if resposta_seguro.upper() != "S":
                    print("Pacote não aceito.")
                    continue
            
            #verifica se o pacote pode ser aceito conforme os parâmetros inseridos
            if peso_a_ser_carregado <= capacidade_peso and volume_carregado + 1 <= capacidade_volume:
                pacotes.append((peso_pacote, valor_mercadoria))
                peso_carregado += peso_pacote
                volume_carregado += 1
                pacotes_carregados += 1
                maior_peso_excedente = max(maior_peso_excedente, adicional_peso)
                maior_valor_excedente = max(maior_valor_excedente, adicional_seguro)
                valor_total_transportado += valor_mercadoria
                valor_total_excedente = adicional_seguro
                print("Pacote aceito. Custo de transporte: R$ ", custo_transporte)
            else:
                print("Pacote não aceito. Capacidade excedida.")
                
        
        elif escolha_parada == "2":
            if pacotes:
                #pop() vai inserir o pacote na última posição da lista
                ultimo_pacote = pacotes.pop()
                peso_pacote, _ = ultimo_pacote
                peso_carregado -= peso_pacote
                volume_carregado -= 1
                print("Pacote retirado. Peso: ", peso_pacote, " kg")
            else:
                print("Não há pacotes para retirar.")
        
        elif escolha_parada == "3":
            maior_quantidade_por_parada = max(maior_quantidade_por_parada, pacotes_carregados)
            if menor_quantidade_por_parada is None:
                menor_quantidade_por_parada = pacotes_carregados
            else:
                menor_quantidade_por_parada = min(menor_quantidade_por_parada, pacotes_carregados)
            
            maior_peso_caminhao_por_parada = max(maior_peso_caminhao_por_parada, peso_carregado)
            if menor_peso_caminhao_por_parada is None:
                menor_peso_caminhao_por_parada = peso_carregado
            else:
                menor_peso_caminhao_por_parada = min(menor_peso_caminhao_por_parada, peso_carregado)
            print("Parada encerrada.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def consultar_situacao():
    global capacidade_peso, peso_carregado, volume_carregado, capacidade_volume, pacotes
    print("\nSituação do Caminhão:")
    print("Peso carregado: ", peso_carregado, " kg")
    print("Peso restante: ", capacidade_peso - peso_carregado, " kg")
    print("Peso máximo: ",capacidade_peso , " kg")
    print("Volume carregado: ", volume_carregado, " m³")
    print("Volume restante: ", capacidade_volume - volume_carregado, " m³")
    print("Volume máximo: ", capacidade_volume, " m³")
    print("Valor transportado: ",valor_total_transportado )
    print("Valor excedente ou restante: ", valor_total_excedente)
    print("Valor padrão máximo: ",seguro_peso_max)

def listar_pacotes():
    global pacotes
    print("\nPacotes no Caminhão:")
    #for vai descompactar as tuplas geradas pelo enumerate
    for i, pacote in enumerate(pacotes):
        peso, _ = pacote
        print("Pacote ", i + 1, ": Peso", peso, " kg")

def gerar_relatorio():
    global pacotes, maior_quantidade_por_parada, menor_quantidade_por_parada, maior_peso_caminhao_por_parada, menor_peso_caminhao_por_parada
    if not pacotes:
        print("Não há pacotes para gerar relatório.")
        return
    
    menor_peso = min(p[0] for p in pacotes)
    maior_peso = max(p[0] for p in pacotes)
    
    print("\n..:: RELATÓRIO DO DIA ::..\n")
    print("Menor peso de pacote individual transportado: {} kg".format(menor_peso))
    print("Maior peso de pacote individual transportado: ", maior_peso, " kg")
    print("Menor quantidade de pacotes embarcados em uma parada: ", menor_quantidade_por_parada)
    print("Maior quantidade de pacotes embarcados em uma parada: ", maior_quantidade_por_parada)
    print("Menor quantidade total de peso no caminhão ao encerrar parada: ", menor_peso_caminhao_por_parada , " Kg")
    print("Maior quantidade total de peso no caminhão ao encerrar parada: ", maior_peso_caminhao_por_parada, " Kg")
    print("Maior peso excedente durante todo dia: ", maior_peso_excedente , " Kg")
    print("Maior valor excedente durante todo dia: R$ ", maior_valor_excedente)

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
            realizar_parada()
        
    elif escolha == "3":
        consultar_situacao()
        
    elif escolha == "4":
        listar_pacotes()
        
    elif escolha == "5":
        print("Dia finalizado.")
        
    elif escolha == "6":
        gerar_relatorio()
        
    elif escolha == "7":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
