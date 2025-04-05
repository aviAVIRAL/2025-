from collections import deque

def bfs(row, col, vis, grid, base_row, base_col):
    n, m = len(grid), len(grid[0])
    vis[row][col] = 1
    q = deque([(row, col)])
    shape = set()
    
    delrow = [-1, 0, 1, 0]
    delcol = [0, 1, 0, -1]
    
    while q:
        r, c = q.popleft()
        shape.add((r - base_row, c - base_col))
        
        for i in range(4):
            nrow, ncol = r + delrow[i], c + delcol[i]
            if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == '1' and not vis[nrow][ncol]:
                vis[nrow][ncol] = 1
                q.append((nrow, ncol))
                
    return frozenset(shape)

def num_unique_islands(grid):
    n, m = len(grid), len(grid[0])
    vis = [[0] * m for _ in range(n)]
    unique_islands = set()
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1' and not vis[i][j]:
                island_shape = bfs(i, j, vis, grid, i, j)
                unique_islands.add(island_shape)
    
    return len(unique_islands)

# Example usage
grid = [
    ['0', '1', '1', '1', '0', '0', '0'],
    ['0', '0', '1', '1', '0', '1', '0']
]

print(num_unique_islands(grid))
