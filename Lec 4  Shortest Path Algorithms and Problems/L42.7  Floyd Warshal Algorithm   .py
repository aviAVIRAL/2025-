

# Floyd Warshal Algorithm



from typing import List

class Solution:
    def shortest_distance(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Step 1: Convert -1 to a large value (simulate infinity)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = int(1e9)
                if i == j:
                    matrix[i][j] = 0

        # Step 2: Run Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]

        # Step 3: Convert "infinity" values back to -1
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == int(1e9):
                    matrix[i][j] = -1

# Driver code
if __name__ == "__main__":
    V = 4
    matrix = [[-1 for _ in range(V)] for _ in range(V)]
    
    matrix[0][1] = 2
    matrix[1][0] = 1
    matrix[1][2] = 3
    matrix[3][0] = 3
    matrix[3][1] = 5
    matrix[3][2] = 4

    obj = Solution()
    obj.shortest_distance(matrix)

    for row in matrix:
        print(" ".join(map(str, row)))



