import time
import copy # Para criar cópias independentes do labirinto para cada simulação
from agentes.agente_entrega import AgenteEntrega
from agentes.agente_controle import AgenteControle
from mapa.labirinto import gerar_labirinto
from heuristicas.funcoes import manhattan, euclidiana, zero_heuristic

def imprimir_labirinto_com_caminho(labirinto, caminho, inicio, fim, titulo="Labirinto com Caminho"):
    """Imprime o labirinto marcando o caminho, início e fim."""
    print(f"\n{titulo}:")
    if not labirinto:
        print("Labirinto vazio.")
        return

    lab_copia = copy.deepcopy(labirinto) # Trabalha em uma cópia para não alterar o original
    if caminho:
        for pos in caminho:
            if pos != inicio and pos != fim:
                lab_copia[pos[0]][pos[1]] = 'o' # Marca o caminho com 'o'
    
    lab_copia[inicio[0]][inicio[1]] = 'S' # Marca o início
    lab_copia[fim[0]][fim[1]] = 'F'       # Marca o fim
    
    for linha in lab_copia:
        print(' '.join(linha))

def executar_simulacao(lab_base, inicio, fim, nome_algoritmo, heuristica_func, custos_terreno_simulacao):
    """
    Executa uma única simulação de busca de caminho e imprime os resultados.
    """
    print(f"--- Iniciando Simulação: {nome_algoritmo} ---")
    # Cria uma cópia do labirinto base para esta simulação específica
    # Isso é crucial se o lab_base já tem tráfego e queremos usá-lo para múltiplos algoritmos
    lab_simulacao = copy.deepcopy(lab_base)

    agente = AgenteEntrega(heuristica=heuristica_func, custos_terreno=custos_terreno_simulacao)
    
    start_time = time.time()
    caminho, nos_expandidos, custo_total = agente.buscar_caminho(lab_simulacao, inicio, fim)
    end_time = time.time()
    
    tempo_execucao = end_time - start_time

    print(f"Algoritmo: {nome_algoritmo}")
    if caminho:
        # print(f"Caminho encontrado: {' -> '.join(map(str, caminho))}") # Opcional: imprimir o caminho detalhado
        print(f"Comprimento do caminho (passos): {len(caminho) - 1}")
        print(f"Custo total do caminho: {custo_total}")
        imprimir_labirinto_com_caminho(lab_simulacao, caminho, inicio, fim, f"Visualização ({nome_algoritmo})")
    else:
        print("Nenhum caminho possível.")
    
    print(f"Nós expandidos: {nos_expandidos}")
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
    print(f"--- Fim da Simulação: {nome_algoritmo} ---\n")

    return {
        "algoritmo": nome_algoritmo,
        "caminho_encontrado": bool(caminho),
        "comprimento_caminho": len(caminho) - 1 if caminho else 0,
        "custo_total": custo_total if caminho else float('inf'),
        "nos_expandidos": nos_expandidos,
        "tempo_execucao": tempo_execucao
    }

def main():
    linhas, colunas = 4, 4
    inicio, fim = (0, 0), (linhas - 1, colunas - 1)

    # Define custos de terreno (pode ser ajustado para testar diferentes impactos de tráfego)
    custos_terreno = {'.': 1, 'T': 5, 'S': 1, 'F': 1, 'o': 1} # Tráfego 'T' tem custo 5

    print("CONFIGURAÇÃO INICIAL:")
    print(f"Mapa: {linhas}x{colunas}, Início: {inicio}, Fim: {fim}")
    print(f"Custos de terreno: {custos_terreno}\n")

    # Lista para armazenar todos os resultados para um resumo final
    todos_resultados = []

    # --- Cenário 1: Com obstáculos e com tráfego ---
    print("============================================================")
    print("=== Cenário 1: 3 Obstáculos, 2 Alertas de Tráfego ===")
    print("============================================================")
    lab_c1 = gerar_labirinto(linhas, colunas, total_barreiras=3, inicio=inicio, fim=fim)
    ag_controle_c1 = AgenteControle(quantidade_alertas=2)
    ag_controle_c1.gerar_alertas_trafego(lab_c1, inicio, fim)
    imprimir_labirinto_com_caminho(lab_c1, None, inicio, fim, "Labirinto Base - Cenário 1") # Mostra o lab com obstáculos e tráfego

    # A* com Manhattan
    res = executar_simulacao(lab_c1, inicio, fim, "A* (Manhattan)", manhattan, custos_terreno)
    todos_resultados.append(res)
    # A* com Euclidiana
    res = executar_simulacao(lab_c1, inicio, fim, "A* (Euclidiana)", euclidiana, custos_terreno)
    todos_resultados.append(res)
    # BFS (A* com heurística zero)
    res = executar_simulacao(lab_c1, inicio, fim, "BFS (Heurística Zero)", zero_heuristic, custos_terreno)
    todos_resultados.append(res)

    # --- Cenário 2: Sem obstáculos, mas com tráfego ---
    print("\n============================================================")
    print("=== Cenário 2: 0 Obstáculos, 2 Alertas de Tráfego ===")
    print("============================================================")
    lab_c2 = gerar_labirinto(linhas, colunas, total_barreiras=0, inicio=inicio, fim=fim) # Sem barreiras
    ag_controle_c2 = AgenteControle(quantidade_alertas=2)
    ag_controle_c2.gerar_alertas_trafego(lab_c2, inicio, fim)
    imprimir_labirinto_com_caminho(lab_c2, None, inicio, fim, "Labirinto Base - Cenário 2")

    res = executar_simulacao(lab_c2, inicio, fim, "A* (Manhattan)", manhattan, custos_terreno)
    todos_resultados.append(res)
    res = executar_simulacao(lab_c2, inicio, fim, "BFS (Heurística Zero)", zero_heuristic, custos_terreno)
    todos_resultados.append(res)

    # --- Cenário 3: Com obstáculos, sem tráfego ---
    print("\n============================================================")
    print("=== Cenário 3: 3 Obstáculos, 0 Alertas de Tráfego ===")
    print("============================================================")
    lab_c3 = gerar_labirinto(linhas, colunas, total_barreiras=3, inicio=inicio, fim=fim)
    # ag_controle_c3 = AgenteControle(quantidade_alertas=0) # Alternativamente, não chamar gerar_alertas_trafego
    # ag_controle_c3.gerar_alertas_trafego(lab_c3, inicio, fim)
    imprimir_labirinto_com_caminho(lab_c3, None, inicio, fim, "Labirinto Base - Cenário 3")

    res = executar_simulacao(lab_c3, inicio, fim, "A* (Manhattan)", manhattan, custos_terreno)
    todos_resultados.append(res)
    res = executar_simulacao(lab_c3, inicio, fim, "BFS (Heurística Zero)", zero_heuristic, custos_terreno)
    todos_resultados.append(res)

    # --- Resumo dos Resultados ---
    print("\n\n============================================================")
    print("--- RESUMO GERAL DOS RESULTADOS ---")
    print("============================================================")
    for i, res in enumerate(todos_resultados):
        print(f"Simulação {i+1}:")
        print(f"  Algoritmo: {res['algoritmo']}")
        print(f"  Caminho Encontrado: {'Sim' if res['caminho_encontrado'] else 'Não'}")
        if res['caminho_encontrado']:
            print(f"  Comprimento (passos): {res['comprimento_caminho']}")
            print(f"  Custo Total: {res['custo_total']}")
        print(f"  Nós Expandidos: {res['nos_expandidos']}")
        print(f"  Tempo de Execução: {res['tempo_execucao']:.6f}s")
        print("-" * 20)

if __name__ == '__main__':
    main()