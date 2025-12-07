from collections import deque

def dfs_init(grid):
    start_col = grid[0].find('S')
    memo = {}
    return beam(0, start_col, 1, 0, grid, memo)

def beam(r, c, dr, dc, grid, memo):
    state = (r, c, dr, dc)

    if state in memo:
        return memo[state]
    
    nr, nc = r + dr, c + dc

    if not (0 <= nr < len(grid) and 0 <= nc < len(grid[r])):
        memo[state] = 1
        return 1
    
    cell = grid[nr][nc]
    if cell != '^':
        res = beam(nr, nc, 1, 0, grid, memo)
        memo[state] = res
        return res
    
    res = beam(nr, nc, 0, -1, grid, memo) + beam(nr, nc, 0, 1, grid, memo)
    memo[state] = res
    return res
    



def bfs_count_split(grid):
    rows = len(grid)
    cols = len(grid[0])

    start_col = grid[0].find('S')

    queue = deque()
    queue.append((0, start_col, 1, 0))  #(row, col, dir_row, dir_col)

    visited = set()

    split_count = 0

    while queue:
        r, c, dr, dc = queue.popleft()

        state = (r, c, dr, dc)
        if state in visited:
            continue
        
        visited.add(state)

        nr, nc = r + dr, c + dc

        if not (0 <= nr < rows and 0 <= nc < cols):
            continue

        cell = grid[nr][nc]
        if cell != '^':
            queue.append((nr, nc, 1, 0))
            continue
        
        split_count += 1

        if nc - 1 >= 0:
            queue.append((nr, nc, 0, -1))
        
        if nc + 1 < cols:
            queue.append((nr, nc, 0, 1))
        
    return split_count

with open('input.txt', 'r') as file:
    content = file.read().splitlines()
    print(dfs_init(content))
    print(bfs_count_split(content))
