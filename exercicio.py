NUM_VEICULOS = 5

def preencheInfoVeiculo():
    print("\n === Cadastro de Veículo ===")
    
    modelo = input("Modelo: ")
    placa = input("Placa (ex: ABC-1234): ")

    try:
        ano = int(input("Ano de fabricação: "))
    except ValueError:
        print("Ano inválido")
        ano = 0
    
    try:
        aluguel = float(input("Valor do aluguel por dia: R$ "))
    except ValueError:
        print(" Valor inválido, usando 0.0...")
        aluguel = 0.0

    return {
        "modelo": modelo,
        "placa": placa,
        "ano": ano,
        "aluguelDia": aluguel
    }

def imprimeVeiculo(veiculo):
    print("\n --- Dados do Veículo ---")
    print(f"Modelo : {veiculo['modelo']}")
    print(f"Placa  : {veiculo['placa']}")
    print(f"Ano    : {veiculo['ano']}")
    print(f"Aluguel/dia: R$ {veiculo['aluguelDia']}")
    print("-------------------------")

def calculaPrecoTotal(frota):
    total = 0
    for v in frota:
        total += v["aluguelDia"]
    return total

def consultaVeiculo(frota, placa):
    placa = placa.upper()
    for i, v in enumerate(frota):
        if v["placa"].upper() == placa:
            return i
    return -1

def editarVeiculo(veiculo):
    while True:
        print("\n === EDITAR VEÍCULO ===")
        imprimeVeiculo(veiculo)

        print("\n O que deseja editar?")
        print("1 - Modelo")
        print("2 - Placa")
        print("3 - Ano")
        print("4 - Aluguel por dia")
        print("5 - Voltar")

        op = input("Opção: ").strip()

        if op == "1":
            novo = input("Novo modelo: ").strip()
            if novo:
                veiculo["modelo"] = novo
                print("Modelo atualizado!")

        elif op == "2":
            nova = input("Nova placa: ").strip().upper()
            if nova:
                veiculo["placa"] = nova
                print("Placa atualizada!")

        elif op == "3":
            novo = input("Novo ano: ").strip()
            if novo:
                try:
                    veiculo["ano"] = int(novo)
                    print("Ano atualizado!")
                except ValueError:
                    print("Ano inválido!")

        elif op == "4":
            novo = input("Novo aluguel por dia: R$ ").strip()
            if novo:
                try:
                    veiculo["aluguelDia"] = float(novo)
                    print("Valor atualizado!")
                except ValueError:
                    print("Valor inválido!")

        elif op == "5":
            break
        else:
            print("Opção inválida!")

def main():
    frota = []

    while True:
        print("\n === Aluguel de Veículos ===")
        print(f"Veículos cadastrados: {len(frota)}/{NUM_VEICULOS}")
        print("1 - Cadastrar veículo")
        print("2 - Consultar por placa")
        print("3 - Somar preço da frota")
        print("4 - Buscar veículo mais novo até certo valor")
        print("5 - Editar veículo")
        print("6 - Sair")

        opcao = input("Opção: ").strip()

        if opcao == "1":
            if len(frota) >= NUM_VEICULOS:
                print("Limite atingido!")
                continue

            novo = preencheInfoVeiculo()

            if consultaVeiculo(frota, novo["placa"]) != -1:
                print("Já existe um veículo com essa placa!")
            else:
                frota.append(novo)
                print("Veículo cadastrado com sucesso!")

        elif opcao == "2":
            placa = input("Digite a placa: ")
            posicao  = consultaVeiculo(frota, placa)
            if posicao  == -1:
                print("Veículo não encontrado.")
            else:
                imprimeVeiculo(frota[posicao ])

        elif opcao == "3":
            total = calculaPrecoTotal(frota)
            print(f"Preço total (1 dia): R$ {total}")

        elif opcao == "4":
            try:
                limite = float(input("Valor máximo: R$ "))
            except ValueError:
                print("Valor inválido!")
                continue

            selecionado = None
            for v in frota:
                if v["aluguelDia"] <= limite:
                    if selecionado is None or v["ano"] > selecionado["ano"]:
                        selecionado = v

            if selecionado:
                imprimeVeiculo(selecionado)
            else:
                print("Nenhum veículo atende aos critérios.")

        elif opcao == "5":
            placa = input("Digite a placa do veículo a editar: ")
            posicao  = consultaVeiculo(frota, placa)
            if posicao  == -1:
                print("Veículo não encontrado.")
            else:
                editarVeiculo(frota[posicao ])

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
