import random

class AgenteControle:
    def __init__(self, quantidade_alertas=2):
        self.quantidade_alertas = quantidade_alertas

    def gerar_alertas_trafego(self, lab, inicio, fim):
        linhas, colunas = len(lab), len(lab[0])

        posicoes_livres = [
            (x, y)
            for x in range(linhas)
            for y in range(colunas)
            if lab[x][y] == '.' and (x, y) != inicio and (x, y) != fim
        ]

        if len(posicoes_livres) < self.quantidade_alertas:
            print(f"Aviso: apenas {len(posicoes_livres)} posições livres para alertas.")
            alertas_para_inserir = len(posicoes_livres)
        else:
            alertas_para_inserir = self.quantidade_alertas

        posicoes_escolhidas = random.sample(posicoes_livres, alertas_para_inserir)

        for x, y in posicoes_escolhidas:
            lab[x][y] = 'T'