


V = 5

# INF = int(1e9)
matrix = [[5] * V for _ in range(V)]

for i in range(V):
    matrix[i][i] = 0

print(matrix) 

# [[0, 5, 5, 5, 5], 
#  [5, 0, 5, 5, 5],
#  [5, 5, 0, 5, 5],
#  [5, 5, 5, 0, 5], 
#  [5, 5, 5, 5, 0]]





