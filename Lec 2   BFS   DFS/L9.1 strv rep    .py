from typing import List

def dfs(row: int, col: int, ans: List[List[int]], image: List[List[int]], 
        newColor: int, delRow: List[int], delCol: List[int], iniColor: int):
    
    ans[row][col] = newColor  
    n, m = len(image), len(image[0])  

    for i in range(4):
        nrow = row + delRow[i]
        ncol=  col + delCol[i]
        
        if (  0 <= nrow < n and 0 <= ncol < m and 
            image[nrow][ncol] == iniColor and 
            ans[nrow][ncol] != newColor ) :
            dfs(nrow, ncol, ans, image, newColor, delRow, delCol, iniColor)
 
def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    iniColor = image[sr][sc]  
    ans = [row[:] for row in image]  # cpoy kr liya 

# up , down , ri, left   :  4  neighbor
    delRow = [-1, 0, 1, 0]
    delCol = [0, 1, 0, -1]

    dfs(sr, sc, ans, image, newColor, delRow, delCol, iniColor)  
    return ans

# Example usage   
image = [ 
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
# ##           (image, sr, sc, newColor:
ans = floodFill(image, 1, 1, 2)

for row in ans:
    print(*row)

# #       op  
# 2 2 2
# 2 2 0
# 2 0 1
