






# Find the City With the Smallest Number of Neighbours at a Threshold Distance: G-43


import sys

class Solution:
    def findCity(self, n, m, edges, distanceThreshold):
        # Initialize distance matrix with "infinity"
        INF = int(1e9)
        dist = [[INF] * n for _ in range(n)]

        # Load edges into distance matrix
        for u, v, wt in edges:
            dist[u][v] = wt
            dist[v][u] = wt  # Since the graph is undirected

        # Distance from a node to itself is 0
        for i in range(n):
            dist[i][i] = 0

        # Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != INF and dist[k][j] != INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # Find the city with minimum reachable cities
        cntCity = n
        cityNo = -1

        for city in range(n):
            cnt = 0
            for adjCity in range(n):
                if dist[city][adjCity] <= distanceThreshold:
                    cnt += 1
            if cnt <= cntCity:
                cntCity = cnt
                cityNo = city

        return cityNo


# Example usage
n = 4
m = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4

obj = Solution()
cityNo = obj.findCity(n, m, edges, distanceThreshold)
print("The answer is node:", cityNo)






