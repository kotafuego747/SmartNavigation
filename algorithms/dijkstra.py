import heapq

moves = [
    (-1, 0),  # yukarı
    ( 1, 0),  # aşağı
    ( 0,-1),  # sol
    ( 0, 1)   # sağ
]


moves = [(-1,0),(1,0),(0,-1),(0,1)]

def isValid(pos, grid):
    row, col = pos
    ROWS, COLS = grid.shape
    return (
        0 <= row < ROWS and
        0 <= col < COLS and
        grid[row, col] != -1
    )



def dijkstra(start, target, grid):
    visited_order = []

    distances = {}
    distances[start] = 0

    parent = {}
    parent[start] = None

    pq = [(0, start)]

    while pq:
        current_weight, current_node = heapq.heappop(pq)
        
        if current_node in visited_order:
            continue

        visited_order.append(current_node)


        if current_node == target:
            break

        if current_weight > distances[current_node]:
            continue


        for dr, dc in moves:
            next_pos = (current_node[0] + dr, current_node[1] + dc)
           
            if isValid(next_pos, grid):
                total_weight = current_weight + grid[next_pos[0], next_pos[1]]

                if next_pos not in distances or total_weight < distances[next_pos]:
                    distances[next_pos] = total_weight
                    parent[next_pos] = current_node
                    heapq.heappush(pq, (total_weight, next_pos))
            
    path = []
    total_cost = None

    # Hedef noktasına ulaşıldı mı kontrol et
    if target in parent:
        cur = target    
        while cur is not None:
            path.insert(0, cur)
            cur = parent.get(cur)
        
        total_cost = distances[target]

    else:
        # Eğer hedef parent içinde yoksa yol bulunamamıştır
        print("UYARI: Başlangıçtan hedefe giden bir yol bulunamadı!")
        path = [] # Boş liste döndür
        total_cost = None

    
    return path, visited_order, total_cost
    
