
# all direct ion 

from collections import deque

def bfs(grid, i, j, vis):
    vis[i][j] = 1
    q = deque([(i, j)])
    n = len(grid) # row 
    m = len(grid[0]) # col 


    while q:
        row, col = q.popleft()
# -------  neighbor travel -------------# ---------------
        
        for del_row in range(-1, 2):  # striver loop  concept   for 8 direction 
            for del_col in range(-1, 2): 
        
                new_row = row + del_row
                new_col = col + del_col
        
                # if (0 <= new_row < n and 0 <= new_col < m and
                #         grid[new_row][new_col] == '1' and not vis[new_row][new_col]):

                if (new_row >=0 and new_row < n and
                    new_col >= 0 and new_col < m and
                    grid[new_row][new_col] == '1' and not vis[new_row][new_col]):
                    
                    vis[new_row][new_col] = 1
                    q.append((new_row, new_col))
# ---------------# ---------------# -----------------
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
    ['0', '1', '1', '0'],
    ['0', '1', '1', '0'],
    ['0', '0', '1', '0'],
    ['0', '0', '0', '0'] , 
    ['1', '1', '0', '1']  ]
print(num_islands(grid)) 
 # Output: 3
# grid = [
#     ['1', '1', '0', '0', '0'],
#     ['1', '1', '0', '0', '0'],
#     ['0', '0', '1', '0', '0'],
#     ['0', '0', '0', '1', '1']  ]
# print(num_islands(grid))  # Output: 3
