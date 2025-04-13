


# Bellman Ford Algorithm: G-41


from typing import List

class Solution:
    def bellman_ford(self, V: int, edges: List[List[int]], S: int) -> List[int]:
        dist = [int(1e8)] * V
        dist[S] = 0
        
        # Relax all edges V - 1 times
        for _ in range(V - 1):
            for u, v, wt in edges:
                if dist[u] != int(1e8) and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
# ----------------------------------------------------------
# You check: can I still relax this edge?
# (dist[u] + wt < dist[v])
# If yes, return [-1] — which means:
# "Hey! There's a negative weight cycle in 
# this graph. I can't give valid shortest paths."

        # Check for negative weight cycle
        for u, v, wt in edges:
            if dist[u] != int(1e8) and dist[u] + wt < dist[v]:
                return [-1]
        
        return dist

# Driver code
if __name__ == "__main__":
    V = 6
    edges = [
        [3, 2, 6],
        [5, 3, 1],
        [0, 1, 5],
        [1, 5, -3],
        [1, 2, -2],
        [3, 4, -2],
        [2, 4, 3]
    ]
    S = 0
    obj = Solution()
    dist = obj.bellman_ford(V, edges, S)
    print(" ".join(map(str, dist)))

