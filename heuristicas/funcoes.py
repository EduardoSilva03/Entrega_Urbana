import math

def manhattan(pos1, pos2):
    """Calcula a distância de Manhattan entre duas posições."""
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def euclidiana(pos1, pos2):
    """Calcula a distância Euclidiana entre duas posições."""
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def zero_heuristic(pos1, pos2):
    """Heurística que sempre retorna zero, usada para algoritmos como BFS/Dijkstra."""
    return 0