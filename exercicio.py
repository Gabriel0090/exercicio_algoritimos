import os

ARQUIVO = "veiculos.txt"

def ler_int(msg, padrao=0):
    try:
        return int(input(msg))
    except ValueError:
        print("Valor inválido. Usando valor padrão.")
        return padrao

def ler_float(msg, padrao=0.0):
    try:
        return float(input(msg))
    except ValueError:
        print("Valor inválido. Usando valor padrão.")
        return padrao

def cadastrar_veiculo():
    print("\n=== Cadastro de Veículo ===")

    modelo  = input("Modelo: ").strip()
    placa   = input("Placa (ex: ABC-1234): ").strip().upper()
    ano     = ler_int("Ano de fabricação: ")
    aluguel = ler_float("Valor do aluguel por dia (R$): ")

    return {
        "modelo": modelo,
        "placa": placa,
        "ano": ano,
        "aluguel": aluguel
    }

def mostrar_veiculo(v):
    print("\n--- Veículo ---")
    print(f"Modelo : {v['modelo']}")
    print(f"Placa  : {v['placa']}")
    print(f"Ano    : {v['ano']}")
    print(f"Aluguel/dia: R$ {v['aluguel']:.2f}")
    print("-------------------")

def encontrar_por_placa(frota, placa):
    placa = placa.upper()
    for i, v in enumerate(frota):
        if v["placa"] == placa:
            return i
    return -1

def editar_veiculo(v):
    while True:
        mostrar_veiculo(v)
        print("\nO que deseja editar?")
        print("1 - Modelo")
        print("2 - Placa")
        print("3 - Ano")
        print("4 - Aluguel por dia")
        print("5 - Voltar")

        op = input("Opção: ")

        if op == "1":
            v["modelo"] = input("Novo modelo: ").strip()
        elif op == "2":
            v["placa"] = input("Nova placa: ").strip().upper()
        elif op == "3":
            v["ano"] = ler_int("Novo ano: ")
        elif op == "4":
            v["aluguel"] = ler_float("Novo aluguel (R$): ")
        elif op == "5":
            break
        else:
            print("Opção inválida.")

        print("✔ Alteração salva!\n")

def salvar_em_arquivo(frota):
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as arq:
            for v in frota:
                arq.write(f"{v['modelo']};{v['placa']};{v['ano']};{v['aluguel']}\n")
        print("\n✔ Dados salvos com sucesso!")
    except Exception as e:
        print("Erro ao salvar:", e)

def carregar_do_arquivo():
    if not os.path.exists(ARQUIVO):
        print("\nNenhum arquivo encontrado.")
        return []

    frota = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arq:
            for linha in arq:
                m, p, a, al = linha.strip().split(";")
                frota.append({
                    "modelo": m,
                    "placa": p,
                    "ano": int(a),
                    "aluguel": float(al)
                })
        print(f"\n✔ {len(frota)} veículos carregados.")
    except Exception as e:
        print("Erro ao carregar arquivo:", e)

    return frota

def main():
    frota = []

    while True:
        print("\n=== Sistema de Aluguel de Veículos ===")
        print(f"Veículos cadastrados: {len(frota)}")

        print("1 - Cadastrar veículo")
        print("2 - Consultar por placa")
        print("3 - Somar preço da frota")
        print("4 - Buscar veículo mais novo até certo valor")
        print("5 - Editar veículo")
        print("6 - Salvar arquivo")
        print("7 - Carregar arquivo")
        print("0 - Sair")

        op = input("Opção: ")

        if op == "1":
            v = cadastrar_veiculo()
            if encontrar_por_placa(frota, v["placa"]) != -1:
                print("Já existe um veículo com essa placa!")
            else:
                frota.append(v)
                print("Veículo cadastrado!")

        elif op == "2":
            placa = input("Placa: ")
            idx = encontrar_por_placa(frota, placa)
            if idx == -1:
                print("Veículo não encontrado.")
            else:
                mostrar_veiculo(frota[idx])

        elif op == "3":
            total = sum(v["aluguel"] for v in frota)
            print(f"Total da frota por 1 dia: R$ {total:.2f}")

        elif op == "4":
            limite = ler_float("Valor máximo: R$ ")

            selecionado = None
            for v in frota:
                if v["aluguel"] <= limite:
                    if selecionado is None or v["ano"] > selecionado["ano"]:
                        selecionado = v

            if selecionado:
                mostrar_veiculo(selecionado)
            else:
                print("Nenhum veículo encontrado com esse valor.")

        elif op == "5":
            placa = input("Placa do veículo: ")
            idx = encontrar_por_placa(frota, placa)
            if idx == -1:
                print("Veículo não encontrado.")
            else:
                editar_veiculo(frota[idx])

        elif op == "6":
            salvar_em_arquivo(frota)

        elif op == "7":
            frota = carregar_do_arquivo()

        elif op == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")

# Execução
if __name__ == "__main__":
    main()
