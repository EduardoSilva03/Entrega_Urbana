import random

def gerar_labirinto(linhas, colunas, total_barreiras, inicio, fim):
    """
    Gera um labirinto (grade) com um número especificado de barreiras.
    'S' (início) e 'F' (fim) não podem ser barreiras.
    """
    # Inicializa o labirinto com todas as células como caminho livre ('.')
    lab = [['.' for _ in range(colunas)] for _ in range(linhas)]

    barreiras_colocadas = 0
    # Tenta colocar o número desejado de barreiras
    # Limita as tentativas para evitar loop infinito se não houver espaço
    tentativas = 0 
    max_tentativas = linhas * colunas * 2 

    while barreiras_colocadas < total_barreiras and tentativas < max_tentativas :
        x, y = random.randint(0, linhas - 1), random.randint(0, colunas - 1)
        # Coloca barreira se a célula está livre ('.') e não é início nem fim
        if lab[x][y] == '.' and (x, y) != inicio and (x, y) != fim:
            lab[x][y] = '|' # Marca a célula como barreira
            barreiras_colocadas += 1
        tentativas +=1
    
    # if barreiras_colocadas < total_barreiras:
        # print(f"Aviso: Não foi possível colocar todas as {total_barreiras} barreiras. Colocadas: {barreiras_colocadas}")

    return lab