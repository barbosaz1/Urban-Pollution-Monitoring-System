import os

# Função 1: Carregar dados de poluição para uma matriz
def carregar_dados(nome_ficheiro):
    try:
        with open(nome_ficheiro, 'r') as ficheiro:
            cabecalho = ficheiro.readline().strip()
            dimensoes = ficheiro.readline().strip().split()
            linhas, colunas = int(dimensoes[0]), int(dimensoes[1])

            matriz = []
            for _ in range(linhas):
                linha = list(map(int, ficheiro.readline().strip().split()))
                matriz.append(linha)

            return cabecalho, matriz
    except FileNotFoundError:
        print("Ficheiro não encontrado.")
        return None, None
    except ValueError:
        print("Erro ao processar o ficheiro. Verifique o formato.")
        return None, None

# Função 2: Mostrar a matriz formatada
def mostrar_matriz(matriz):
    if not matriz:
        print("Matriz não carregada.")
        return

    for linha in matriz:
        print(" ".join(f"{valor:>4}" for valor in linha))

# Função 3: Gerar Mapa de Alertas de Poluição (PAM)
def gerar_pam(matriz):
    if not matriz:
        print("Matriz não carregada.")
        return []

    def obter_alerta(valor):
        if valor < 19:
            return 'M'
        elif valor < 30:
            return 'H'
        elif valor < 40:
            return 'E'
        else:
            return 'S'

    return [[obter_alerta(valor) for valor in linha] for linha in matriz]

# Função 4: Ajustar níveis de poluição
def ajustar_poluicao(matriz, ajuste):
    if not matriz:
        print("Matriz não carregada.")
        return []

    return [[valor + ajuste for valor in linha] for linha in matriz]

# Função 5: Calcular percentagem de níveis de alerta
def calcular_percentagens(pam):
    if not pam:
        print("PAM não gerado.")
        return

    total_areas = sum(len(linha) for linha in pam)
    contagem = {"M": 0, "H": 0, "E": 0, "S": 0}

    for linha in pam:
        for alerta in linha:
            contagem[alerta] += 1

    for alerta, valor in contagem.items():
        percentagem = (valor / total_areas) * 100
        print(f"{alerta}: {percentagem:.2f}%")

# Função 6: Encontrar aumento necessário para nível "Severe"
def encontrar_aumento_severe(matriz):
    if not matriz:
        print("Matriz não carregada.")
        return

    max_atual = max(max(linha) for linha in matriz)
    aumento = max(0, 40 - max_atual)
    print(f"Aumento necessário para todos atingirem 'Severe': {aumento} µg/m³")

# Interface principal
def interface():
    matriz = None
    cabecalho = None

    while True:
        print("\nMenu Principal:")
        print("1. Carregar dados de poluição")
        print("2. Mostrar matriz de poluição")
        print("3. Gerar PAM")
        print("4. Ajustar níveis de poluição")
        print("5. Calcular percentagens de alertas")
        print("6. Encontrar aumento para 'Severe'")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome_ficheiro = input("Nome do ficheiro: ")
            cabecalho, matriz = carregar_dados(nome_ficheiro)
        elif escolha == "2":
            mostrar_matriz(matriz)
        elif escolha == "3":
            pam = gerar_pam(matriz)
            mostrar_matriz(pam)
        elif escolha == "4":
            try:
                ajuste = int(input("Valor de ajuste: "))
                matriz = ajustar_poluicao(matriz, ajuste)
            except ValueError:
                print("Insira um número válido.")
        elif escolha == "5":
            pam = gerar_pam(matriz)
            calcular_percentagens(pam)
        elif escolha == "6":
            encontrar_aumento_severe(matriz)
        elif escolha == "0":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    interface()
