import numpy as np
import random

ROWS = 10
COLS = 10

def create_grid_bfs_dfs():
   
    grid = np.array([
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    ])
    return grid


def create_dijkstra():
    grid = np.zeros((ROWS, COLS), dtype=int)  # Dijkstra için rastgele maliyetli 10x10 grid oluşturur.

    for r in range(ROWS):
        for c in range(COLS):
            chance = random.random()
            if chance < 0.10:
                grid[r][c] = -1       # engel
            elif chance < 0.45:
                grid[r][c] = 1        # akıcı
            elif chance < 0.75:
                grid[r][c] = 3        # orta
            else:
                grid[r][c] = 6        # yoğun
    
    return grid
                



def create_bellman_ford():
    grid = np.zeros((ROWS, COLS), dtype=int)

    for r in range(ROWS):
        for c in range(COLS):
            chance = random.random()
            if chance < 0.15:
                grid[r][c] = -1    # Bina / Engel
            elif chance < 0.45:
                grid[r][c] = 1     # Akıcı (Maliyet 1)
            elif chance < 0.65:
                grid[r][c] = 6     # Çok Yoğun (Maliyet 6)
            elif chance < 0.85:
                grid[r][c] = 3     # Orta (Maliyet 3)
            else:
                grid[r][c] = 0     # BELEŞ YOL (Maliyet 0) -> %15 ihtimal
    
    return grid