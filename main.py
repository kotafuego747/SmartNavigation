from algorithms.bfs import bfs  #  bfs (soldaki) → bfs.py dosyası ,  bfs (sağdaki) → o dosyanın içindeki bfs() fonksiyonu
from algorithms.dfs import dfs
from algorithms.dijkstra import dijkstra
from algorithms.bellman_ford import bellman_ford

from grid.grid import create_grid_bfs_dfs, create_dijkstra, create_bellman_ford

from visualize.visualize import animate 
from visualize.visualize_dijkstra import animate_dijkstra
from visualize.visualize_bellman_ford import animate_bellman_ford


ALGO = "BELLMANFORD"   # "BFS", "DFS", "DIJKSTRA", "BELLMANFORD"

START = (0, 0)      # Robotun Başlangıç Kordinatı
TARGET = (5, 5)     #  Robotun Varacağı Hedef Kordinatı
     

if ALGO == "BFS":
    grid = create_grid_bfs_dfs()
    grid[START] = 0
    grid[TARGET] = 0

    path, visited_order = bfs(START, TARGET, grid)
    animate(grid, START, TARGET, path, visited_order, "BFS")


elif ALGO == "DFS":
    grid = create_grid_bfs_dfs()
    grid[START] = 0
    grid[TARGET] = 0

    path, visited_order = dfs(START, TARGET, grid)
    animate(grid, START, TARGET, path, visited_order, "DFS")


elif ALGO == "DIJKSTRA":
    grid = create_dijkstra()
    grid[START] = 1
    grid[TARGET] = 1

    path, visited_order, total_cost = dijkstra(START, TARGET, grid)
    animate_dijkstra(grid, START, TARGET, path, visited_order, total_cost)

elif ALGO == "BELLMANFORD":
    grid = create_bellman_ford()
    
    # Başlangıç ve hedefi güvenli (maliyetsiz) hale getirelim
    grid[START] = 0
    grid[TARGET] = 0

    # Algoritmayı çalıştır
    path, visited_order, total_cost = bellman_ford(START, TARGET, grid)
    animate_bellman_ford(grid, START, TARGET, path, visited_order, total_cost)
    