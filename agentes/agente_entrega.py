import heapq

class AgenteEntrega:
    def __init__(self, heuristica, custos_terreno=None):
        """
        Inicializa o Agente de Entrega.
        :param heuristica: Função heurística a ser usada (ex: manhattan, euclidiana, zero_heuristic).
        :param custos_terreno: Dicionário com os custos para cada tipo de célula.
        """
        self.heuristica = heuristica if heuristica else lambda a, b: 0 # Padrão para heurística zero se None
        # Custos padrão para diferentes tipos de terreno/célula
        self.custos_terreno = custos_terreno if custos_terreno else {
            '.': 1,  # Caminho livre
            'T': 3,  # Tráfego (custo maior)
            'S': 1,  # Início
            'F': 1,  # Fim
            'o': 1   # Célula parte do caminho já marcada (não deve ocorrer durante a busca)
        }

    def buscar_caminho(self, labirinto, inicio, destino):
        """
        Busca um caminho do início ao destino usando um algoritmo baseado em A*
        (que se torna Dijkstra/BFS se a heurística for zero).
        Retorna o caminho, número de nós expandidos e o custo total.
        """
        # Fronteira é uma fila de prioridade: (f_score, g_score, posição)
        # g_score é o custo do início até a posição atual
        # f_score é g_score + heurística(posição_atual, destino)
        fronteira = [(self.heuristica(inicio, destino), 0, inicio)]
        origem = {inicio: None}  # Dicionário para reconstruir o caminho (vizinho: predecessor)
        custo_ate_agora = {inicio: 0} # g_score
        nos_expandidos = 0

        while fronteira:
            _, custo_atual_g, atual = heapq.heappop(fronteira)
            nos_expandidos += 1

            if atual == destino: # Destino alcançado
                caminho = []
                temp = destino
                while temp is not None: # Reconstrói o caminho do destino ao início
                    caminho.append(temp)
                    temp = origem[temp]
                return caminho[::-1], nos_expandidos, custo_ate_agora[destino] # Retorna caminho, nós, custo

            # Explora vizinhos (movimentos cardinais: cima, baixo, esquerda, direita)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                vizinho = (atual[0] + dx, atual[1] + dy)

                # Verifica se o vizinho está dentro dos limites do labirinto
                if 0 <= vizinho[0] < len(labirinto) and 0 <= vizinho[1] < len(labirinto[0]):
                    tipo_celula_vizinho = labirinto[vizinho[0]][vizinho[1]]

                    if tipo_celula_vizinho == '|':  # Obstáculo ('|') é intransponível
                        continue

                    # Calcula o custo do movimento para o vizinho
                    custo_movimento = self.custos_terreno.get(tipo_celula_vizinho, 1) # Padrão 1 se tipo não em custos

                    novo_custo_g = custo_ate_agora[atual] + custo_movimento

                    # Se o vizinho não foi visitado ou um caminho mais barato foi encontrado
                    if vizinho not in custo_ate_agora or novo_custo_g < custo_ate_agora[vizinho]:
                        custo_ate_agora[vizinho] = novo_custo_g
                        prioridade_f = novo_custo_g + self.heuristica(vizinho, destino)
                        heapq.heappush(fronteira, (prioridade_f, novo_custo_g, vizinho))
                        origem[vizinho] = atual
        
        # Nenhum caminho encontrado
        return None, nos_expandidos, float('inf')