
#   4 direct ion only 

from collections import deque

def bfs(grid, i, j, vis):
    vis[i][j] = 1
    q = deque([(i, j)])
    n = len(grid)  # row count
    m = len(grid[0])  # column count
    
    # 4 only directions: up, down, left, right
    directions = [(-1, 0), (+1, 0), (0, -1), (0, +1)]   # Up, Down, Left, Right

# --------     
# # see afro all  8 direction 
#  directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  # Up, Down, Left, Right
#                   (-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonal directions
# --------     


    while q:
        row, col = q.popleft()
        for del_row, del_col in directions:
            new_row = row + del_row
            new_col = col + del_col

            if (0 <= new_row < n and
                0 <= new_col < m and
                grid[new_row][new_col] == '1' and not vis[new_row][new_col]):

                vis[new_row][new_col] = 1
                q.append((new_row, new_col))

def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    vis = [[0] * cols for _ in range(rows)]
    count = 0
    for i in range(rows):
        for j in range(cols):
            if not vis[i][j] and grid[i][j] == '1':
                bfs(grid, i, j, vis)
                count += 1
    return count

# Example usage
grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
print(num_islands(grid))  # Output: 3
