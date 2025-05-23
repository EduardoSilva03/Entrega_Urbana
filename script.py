import random
import heapq

# Tamanho do labirinto
linhas, colunas = 4, 4
labirinto = [['.' for _ in range(colunas)] for _ in range(linhas)]

# Adicionar barreiras aleatórias (exceto início e fim)
total_barreiras = 5
while total_barreiras > 0:
    x, y = random.randint(0, linhas - 1), random.randint(0, colunas - 1)
    if labirinto[x][y] == '.' and (x, y) not in [(0, 0), (linhas - 1, colunas - 1)]:
        labirinto[x][y] = '|'
        total_barreiras -= 1

# Heurística: Distância de Manhattan
def manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# Algoritmo A*
def buscar_caminho(lab, inicio, destino):
    fronteira = [(manhattan(inicio, destino), 0, inicio)]
    origem = {}
    custo_ate_agora = {inicio: 0}

    while fronteira:
        _, custo_atual, atual = heapq.heappop(fronteira)

        if atual == destino:
            caminho = []
            while atual in origem:
                caminho.append(atual)
                atual = origem[atual]
            return [inicio] + caminho[::-1]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            vizinho = (atual[0] + dx, atual[1] + dy)
            if 0 <= vizinho[0] < linhas and 0 <= vizinho[1] < colunas:
                if lab[vizinho[0]][vizinho[1]] == '|':
                    continue
                novo_custo = custo_atual + 1
                if vizinho not in custo_ate_agora or novo_custo < custo_ate_agora[vizinho]:
                    custo_ate_agora[vizinho] = novo_custo
                    prioridade = novo_custo + manhattan(vizinho, destino)
                    heapq.heappush(fronteira, (prioridade, novo_custo, vizinho))
                    origem[vizinho] = atual
    return None

# Definir início e fim
inicio, fim = (0, 0), (linhas - 1, colunas - 1)
caminho = buscar_caminho(labirinto, inicio, fim)

# Marcar caminho no labirinto
if caminho:
    for pos in caminho:
        if pos not in [inicio, fim]:
            labirinto[pos[0]][pos[1]] = 'o'

# Marcar início e fim
labirinto[inicio[0]][inicio[1]] = 'S'
labirinto[fim[0]][fim[1]] = 'F'

# Exibir labirinto
print("\nLabirinto com caminho:")
for linha in labirinto:
    print(' '.join(linha))

# Exibir coordenadas do caminho
print("\nCaminho encontrado:")
if caminho:
    print(' '.join(map(str, caminho)))
else:
    print("Nenhum caminho possível.")