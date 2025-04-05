


# 8 quetion   link gfg   

# https://www.geeksforgeeks.org/problems/find-the-number-of-islands/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find_the_number_of_islands


from collections import deque

def bfs(grid, i, j, vis):
    vis[i][j] = 1
    q = deque([(i, j)])
    rows, cols = len(grid), len(grid[0])

 # only for 4 direction
    del_row = [-1, 0, 1, 0]
    del_col = [0, 1, 0, -1]

    while q:
        r, c = q.popleft()

        for k in range(4):
            new_row = r + del_row[k]
            new_col = c + del_col[k]

            if (0 <= new_row < rows and 0 <= new_col < cols and
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


