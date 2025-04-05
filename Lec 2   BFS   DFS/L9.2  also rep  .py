from typing import List

def dfs(row: int, col: int, ans: List[List[int]], image: List[List[int]], 
        newColor: int, iniColor: int):
    
    ans[row][col] = newColor  
    n, m = len(image), len(image[0])  

    delRow = [-1, 0, 1, 0]
    delCol = [0, 1, 0, -1]

    for i in range(4):
        nrow = row + delRow[i]
        ncol = col + delCol[i]
        
        if (0 <= nrow < n and 0 <= ncol < m and 
            image[nrow][ncol] == iniColor and 
            ans[nrow][ncol] != newColor):
            dfs(nrow, ncol, ans, image, newColor, iniColor)
 
def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    iniColor = image[sr][sc]  
    ans = [row[:] for row in image]  

    dfs(sr, sc, ans, image, newColor, iniColor)  
    return ans

# Example usage   
image = [ 
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
ans = floodFill(image, 1, 1, 2)

for row in ans:
    print(*row)
