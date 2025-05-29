from agentes.agente_entrega import AgenteEntrega
from agentes.agente_controle import AgenteControle
from mapa.labirinto import gerar_labirinto
from heuristicas.funcoes import manhattan, euclidiana

linhas, colunas = 4, 4
inicio, fim = (0, 0), (linhas - 1, colunas - 1)

lab = gerar_labirinto(linhas, colunas, total_barreiras=3, inicio=inicio, fim=fim)

controle = AgenteControle(quantidade_alertas=2)
controle.gerar_alertas_trafego(lab, inicio, fim)

entrega = AgenteEntrega(heuristica=manhattan)  # ou euclidiana
caminho = entrega.buscar_caminho(lab, inicio, fim)

if caminho:
    for pos in caminho:
        if pos not in [inicio, fim]:
            lab[pos[0]][pos[1]] = 'o'

lab[inicio[0]][inicio[1]] = 'S'
lab[fim[0]][fim[1]] = 'F'

print("\nLabirinto com caminho:")
for linha in lab:
    print(' '.join(linha))

print("\nCaminho encontrado:")
if caminho:
    print(' -> '.join(map(str, caminho)))
else:
    print("Nenhum caminho possível.")