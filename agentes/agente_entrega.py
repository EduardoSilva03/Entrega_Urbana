import heapq
from heuristicas.funcoes import manhattan, euclidiana

class AgenteEntrega:
    def __init__(self, heuristica):
        self.heuristica = heuristica

    def buscar_caminho(self, labirinto, inicio, destino):
        fronteira = [(self.heuristica(inicio, destino), 0, inicio)]
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

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                vizinho = (atual[0] + dx, atual[1] + dy)
                if 0 <= vizinho[0] < len(labirinto) and 0 <= vizinho[1] < len(labirinto[0]):
                    if labirinto[vizinho[0]][vizinho[1]] == '|':
                        continue
                    novo_custo = custo_atual + 1
                    if vizinho not in custo_ate_agora or novo_custo < custo_ate_agora[vizinho]:
                        custo_ate_agora[vizinho] = novo_custo
                        prioridade = novo_custo + self.heuristica(vizinho, destino)
                        heapq.heappush(fronteira, (prioridade, novo_custo, vizinho))
                        origem[vizinho] = atual
        return None