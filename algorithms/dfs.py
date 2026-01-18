
moves = [
    (-1, 0),  # yukarı
    ( 1, 0),  # aşağı
    ( 0,-1),  # sol
    ( 0, 1)   # sağ
]


def isValid(pos, grid):
    row, col = pos
    ROWS, COLS = grid.shape

    return (
        0 <= row < ROWS  and 
        0 <= col < COLS  and 
        grid[row, col] != 1
    )



def dfs(start, target, grid):
    visited = set()
    visited_order = []
    parent = {}
    parent[start] = None

    def dfs_recursive(current):

        visited.add(current)
        visited_order.append(current)

        if current == target:
            return True

        for dr, dc in moves:
            next_pos = (current[0] + dr, current[1] + dc)
            if isValid(next_pos, grid) and next_pos not in visited:
                parent[next_pos] = current
                if dfs_recursive(next_pos):
                    return True
        
        return False

    path = []
    if dfs_recursive(start):     
        cur = target
        while cur is not None:
            path.insert(0, cur)
            cur = parent[cur]
        
    return path, visited_order

