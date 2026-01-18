import numpy as np

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def isValid(pos, grid):
    row, col = pos
    ROWS, COLS = grid.shape
    return (0 <= row < ROWS and 0 <= col < COLS and grid[row, col] != -1)

def bellman_ford(start, target, grid):
    ROWS, COLS = grid.shape
    nodes = [(r, c) for r in range(ROWS) for c in range(COLS)]
    
    # Başlatma
    distance = {node: float('inf') for node in nodes}
    distance[start] = 0
    predecessor = {node: None for node in nodes}
    visited_order = []

    # --- AŞAMA 1: KENAR GEVŞETME (V-1 KEZ) ---
    # Bu aşamanın sonunda negatif döngü yoksa en kısa yollar bulunmuş olur.
    for _ in range(len(nodes) - 1):
        for u in nodes:
            r, c = u
            if distance[u] == float('inf') or grid[r, c] == -1:
                continue
            
            for dr, dc in moves:
                v = (r + dr, c + dc)
                if isValid(v, grid):
                    weight = grid[v[0], v[1]]
                    if distance[u] + weight < distance[v]:
                        distance[v] = distance[u] + weight
                        predecessor[v] = u
                        visited_order.append(v)

    # --- AŞAMA 2: NEGATİF DÖNGÜ TESPİTİ ---
    # Eğer bu aşamada hala bir mesafe kısalıyorsa, orada negatif bir döngü vardır!
    negative_cycle = False
    for u in nodes:
        r, c = u
        if distance[u] == float('inf') or grid[r, c] == -1:
            continue
            
        for dr, dc in moves:
            v = (r + dr, c + dc)
            if isValid(v, grid):
                weight = grid[v[0], v[1]]
                # Eğer hala daha kısa bir yol bulunabiliyorsa:
                if distance[u] + weight < distance[v]:
                    negative_cycle = True
                    break
        if negative_cycle: break

    if negative_cycle:
        print("!!! DİKKAT: SİSTEMDE NEGATİF DÖNGÜ TESPİT EDİLDİ !!!")
        # Negatif döngü varsa yol hesaplanamaz çünkü maliyet sonsuza kadar düşer.
        return [], visited_order, None

    # Yolu Geriye Doğru Oluştur (Backtracking)
    path = []
    if distance[target] != float('inf'):
        curr = target
        while curr is not None:
            path.insert(0, curr)
            curr = predecessor[curr]

    total_cost = distance[target] if distance[target] != float("inf") else None
            
    return path, visited_order, total_cost