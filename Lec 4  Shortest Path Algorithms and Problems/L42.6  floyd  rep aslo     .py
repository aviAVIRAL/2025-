

# .........



from typing import List, Tuple

def floyd_warshall_from_edges(V: int, edges: List[Tuple[int, int, int]]) -> List[List[int]]:
    # Step 1: Create adjacency matrix

    # matrix = [[int(1e9) if i != j else 0 for j in range(V)] for i in range(V)]
# also repre as 
    matrix = [[int(1e9)] * V for _ in range(V)]
    for i in range(V):
        matrix[i][i] = 0

    print()
    print(matrix)
    print()

# [[0, 1000000000, 1000000000, 1000000000],
#  [1000000000, 0, 1000000000, 1000000000],
#  [1000000000, 1000000000, 0, 1000000000],
#  [1000000000, 1000000000, 1000000000, 0]]

    for u, v, wt in edges:
        matrix[u][v] = wt  # directed edge

# [[0, 2, 1000000000, 1000000000],
#  [1, 0, 3, 1000000000],
#  [1000000000, 1000000000, 0, 1000000000],
#  [3, 5, 4, 0]] 


    print()
    print(matrix)
    print()
    # Step 2: Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

    # Step 3: Convert infinity back to -1
    for i in range(V):
        for j in range(V):
            if matrix[i][j] == int(1e9):
                matrix[i][j] = -1

    return matrix


# 🔧 Driver code
if __name__ == "__main__":
    V = 4
    edges = [
        (0, 1, 2),
        (1, 0, 1),
        (1, 2, 3),
        (3, 0, 3),
        (3, 1, 5),
        (3, 2, 4)
    ]

    Ans = floyd_warshall_from_edges(V, edges)

    for row in Ans:
        print(*row)

# # op 


# 0 2 5 -1
# 1 0 3 -1  
# -1 -1 0 -1
# 3 5 4 0





