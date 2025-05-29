import random

def gerar_labirinto(linhas, colunas, total_barreiras, inicio, fim):
    lab = [['.' for _ in range(colunas)] for _ in range(linhas)]

    while total_barreiras > 0:
        x, y = random.randint(0, linhas - 1), random.randint(0, colunas - 1)
        if lab[x][y] == '.' and (x, y) not in [inicio, fim]:
            lab[x][y] = '|'
            total_barreiras -= 1

    return lab