import random

class AgenteControle:
    def __init__(self, quantidade_alertas=2):
        self.quantidade_alertas = quantidade_alertas

    def gerar_alertas_trafego(self, lab, inicio, fim):
        """
        Gera alertas de tráfego ('T') em posições aleatórias do labirinto.
        Não modifica as posições de início e fim.
        """
        linhas, colunas = len(lab), len(lab[0])

        posicoes_livres = [
            (x, y)
            for x in range(linhas)
            for y in range(colunas)
            # Garante que a célula está livre ('.') e não é início ou fim
            if lab[x][y] == '.' and (x, y) != inicio and (x, y) != fim
        ]

        # Determina quantos alertas podem ser realmente inseridos
        if len(posicoes_livres) < self.quantidade_alertas:
            # print(f"Aviso: apenas {len(posicoes_livres)} posições livres para alertas de tráfego.")
            alertas_para_inserir = len(posicoes_livres)
        else:
            alertas_para_inserir = self.quantidade_alertas

        if alertas_para_inserir > 0:
            posicoes_escolhidas = random.sample(posicoes_livres, alertas_para_inserir)
            for x, y in posicoes_escolhidas:
                lab[x][y] = 'T' # Marca a célula com tráfego