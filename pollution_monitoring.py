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
def obter_alerta(valor):
        if valor < 19:
            return 'M'
        elif valor < 30:
            return 'H'
        elif valor < 40:
            return 'E'
        else:
            return 'S'
            
def gerar_pam(matriz):
    if not matriz:
        print("Matriz não carregada.")
        return []

    return [[obter_alerta(valor) for valor in linha] for linha in matriz]

# Função 4: Ajustar níveis de poluição
def ajustar_poluicao(matriz, ajuste): #o ajuste é o valor que será somado a cada elemento da matriz
    if not matriz: #verificação se a matriz está vazia
        print("Matriz não carregada.") #caso a matriz esteja vazia
        return []

    return [[valor + ajuste for valor in linha] for linha in matriz] #criação de uma nova matriz onde cada valor é ajustado pelo valor "ajuste"
#for linha in matriz percorre cada linha na matriz 
#for valor in linha percorre cada valor na dentro da linha
#valor + ajuste a cada valor da linha, o valor de ajuste é somado

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

# Função 7: Efeito do Controle de Poluição
def efeito_controle_poluicao(matriz, ajuste):
    if not matriz:
        print("Matriz não carregada.")
        return None, 0

    matriz_ajustada = ajustar_poluicao(matriz, ajuste)
    pam_antigo = gerar_pam(matriz)
    pam_novo = gerar_pam(matriz_ajustada)

    alteracoes = sum(1 for i in range(len(pam_antigo)) for j in range(len(pam_antigo[0])) if pam_antigo[i][j] != pam_novo[i][j])
    total_areas = len(pam_antigo) * len(pam_antigo[0])
    percentagem = (alteracoes / total_areas) * 100

    return matriz_ajustada, percentagem

# Função 9: Identificar Local Ideal para Redução de Poluição
def identificar_local_reducao(matriz):
    if not matriz:
        print("Matriz não carregada.")
        return "Sem dados."

    linhas, colunas = len(matriz), len(matriz[0])
    max_poluição = 0
    melhor_local = None

    for i in range(linhas - 2):
        for j in range(colunas - 2):
            soma = sum(matriz[x][y] for x in range(i, i + 3) for y in range(j, j + 3))
            if soma > max_poluição:
                max_poluição = soma
                melhor_local = (i, j)

    return melhor_local if melhor_local else "Nenhuma área encontrada."

# Função 10: Determinar Coluna Segura
def determinar_coluna_segura(matriz):
    if not matriz:
        print("Matriz não carregada.")
        return "Sem dados."

    colunas = len(matriz[0])
    for j in range(colunas - 1, -1, -1):
        if all(linha[j] < 40 for linha in matriz):
            return j

    return "Nenhuma coluna segura encontrada."

# Função 8: Simular Propagação de Poluição com Vento
def simular_propagacao_vento(matriz): #recebe a variável matriz
    if not matriz: #verificação se a matriz está vazia
        print("Matriz não carregada.") #caso a matriz esteja vazia
        return []

    linhas = len(matriz) #numero de linhas da matriz 
    colunas = len(matriz[0]) #número de colunas da matriz
    nova_matriz = [linha[:] for linha in matriz]
#cria uma cópia da matriz original. Isso é feito para que as mudanças que a função faz na matriz não afetem o processamento de outras funções, para a matriz original não ser alterada
    for i in range(1, linhas): #percorre as linhas da matriz a começar na segunda linha (indice 1) até á ultima linha, começa em 1 porque a propagação da poluição depende da linha anterior
        for j in range(colunas): #a cada iteração do loop externo (que percorre as linhas), o loop interno percorre as colunas dessa linha
            if matriz[i - 1][j] >= 40:#verifica se o valor de poluição da célula na linha anterior (linha i - 1) na mesma coluna (j) é maior ou igual a 40
                nova_matriz[i][j] = max(nova_matriz[i][j], 40) #verifica se a variavel atual (nova_matriz[i][j]) já tem um valor maior ou igual a 40. Caso contrário, ela ajusta o valor da variável para 40

    return nova_matriz

# Função Extra 12: Identificar Regiões Contíguas Acima de um Limite
def identificar_regioes_contiguas(matriz, limite):
    if not matriz:
        print("Matriz não carregada.")
        return []

    linhas = len(matriz)
    colunas = len(matriz[0])
    visitado = [[False] * colunas for _ in range(linhas)]
    regioes = []

    def dfs(x, y, regiao):
        if x < 0 or x >= linhas or y < 0 or y >= colunas or visitado[x][y] or matriz[x][y] <= limite:
            return
        visitado[x][y] = True
        regiao.append((x, y))
        dfs(x + 1, y, regiao)
        dfs(x - 1, y, regiao)
        dfs(x, y + 1, regiao)
        dfs(x, y - 1, regiao)

    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] > limite and not visitado[i][j]:
                regiao = []
                dfs(i, j, regiao)
                regioes.append(regiao)

    return regioes

# Função Extra 16: Previsão de Níveis de Poluição
def prever_poluicao(matriz, taxa):
    if not matriz:
        print("Matriz não carregada.")
        return []

    return [[int(valor * (1 + taxa / 100)) for valor in linha] for linha in matriz]

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
        print("7. Efeito do controle de poluição")
        print("8. Simular propagação de poluição com vento")
        print("9. Identificar local ideal para redução de poluição")
        print("10. Determinar coluna segura")
        print("11. Identificar regiões contíguas acima de um limite")
        print("12. Previsão de níveis de poluição")
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
        elif escolha == "7":
            try:
                ajuste = int(input("Ajuste para simulação: "))
                matriz, percentagem = efeito_controle_poluicao(matriz, ajuste)
                print(f"Percentagem de áreas alteradas: {percentagem:.2f}%")
            except ValueError:
                print("Insira um número válido.")
        elif escolha == "8":
            matriz = simular_propagacao_vento(matriz)
            print("Propagação simulada:")
            mostrar_matriz(matriz)
        elif escolha == "9":
            local = identificar_local_reducao(matriz)
            print(f"Local ideal para redução: {local}")
        elif escolha == "10":
            coluna = determinar_coluna_segura(matriz)
            print(f"Coluna segura: {coluna}")
        elif escolha == "11":
            try:
                limite = int(input("Limite para regiões contíguas: "))
                regioes = identificar_regioes_contiguas(matriz, limite)
                print(f"Regiões contíguas acima de {limite}: {regioes}")
            except ValueError:
                print("Insire um número válido.")
        elif escolha == "12":
            try:
                taxa = float(input("Taxa de previsão (%): "))
                matriz = prever_poluicao(matriz, taxa)
                print("Previsão da poluição aplicada:")
                mostrar_matriz(matriz)
            except ValueError:
                print("Insire um número válido.")
        elif escolha == "0":
            print("A sair programa.")
            break
        else:
            print("Opção inválida. Tenta novamente.")

if __name__ == "__main__":
    interface()
