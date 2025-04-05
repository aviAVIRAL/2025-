
# striver frost represntation  

from collections import deque
from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
     
    vis = [[0] * m for _ in range(n)]
    q = deque()
    # cntFresh = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append((i, j, 0))  # Store (row, col, time)
                vis[i][j] = 2
            else : # no need towrite as alredy o hai 
                vis[i][j] == 0
                # cntFresh += 1  # Count fresh oranges
# -----------------------------------------------------

    delRow = [-1, 0, +1, 0]
    delCol = [0, +1, 0, -1]

    maxTime = 0
    # cnt = 0  

    while q:
        r, c, t = q.popleft()
        maxTime = max(maxTime, t)

        for i in range(4):
            nRow = r + delRow[i]
            nCol = c + delCol[i]

            if (0 <= nRow < n and 0 <= nCol < m and
    vis[nRow][nCol] != 2 and grid[nRow][nCol] == 1):
 #  vis[nRow][nCol] == 0 and grid[nRow][nCol] == 1):
   
                q.append((nRow, nCol, t + 1)) 
                vis[nRow][nCol] = 2  
                # cnt += 1 
#  -  -  -  -  -   -  -  -  - -  -  -  -  -  -  -  -  -  
    for i in range(n):
        for j in range(m):
            if vis[i][j] != 2 and grid[i][j] == 1: 
                return -1 
    return maxTime
    # return -1 if cnt != cntFresh else maxTime

# Example usage
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
rotting_time = orangesRotting(grid)
print("Minimum Number of Minutes Required:", rotting_time)



