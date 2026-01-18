from collections import deque

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
      grid[row][col] != 1
    )


def bfs(start, target, grid):
    visited = set()
    visited.add(start)

    visited_order = []  # Matplotlible daha önce visited edilen yerleri gösteriyor. Array oluşturdum bunun için çünkü yukardaki set tipinde olan visited kullansam doğru sırayla göstermezdi çünkü visited verileri sırası karışık şekilde tutar ama array sıralı şekilde tutar. Set şeklinde tutunca bir veri set içinde var mı kolayca bulunur onun amacı kontrol amaçlı.

    parent = {}  # Dikkat et bu set değil dictionary.  Set yukardaki gibi tanımlanır.  {"A": "B", "C": "D"} şeklinde yazıyorsan bu dictionary'dir. Eğer {"A","B"} şeklinde yazıyorsan bu set'dir. Yani arada iki nokta olursa dictionary'dir ve yandaki gibi boş olarka tanımlanır ama iki nokta yoksa set'dir ve üstteki gibi boş olarak tnaımlanır.
    parent[start] = None

    dq = deque([(start)])

    while dq:
        current = dq.popleft()
        visited_order.append(current)

        if current == target:
            break

        for dr, dc in moves:    # dr= delta row(satırdaki değişim),  dc = delta column(sütundaki değişim)
            next_pos = (current[0] + dr, current[1] + dc)

            if isValid(next_pos, grid) and next_pos not in visited:
                visited.add(next_pos)
                dq.append(next_pos)
                parent[next_pos] = current
    
    path = []
    cur = target
    while cur is not None:
        path.insert(0, cur)
        cur = parent[cur]

    return path, visited_order




