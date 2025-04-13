







# G-40: Number of Ways to Arrive at Destination   


import heapq
from collections import defaultdict

def countPaths( n, roads):
    # Create adjacency list
    adj = defaultdict(list)
    for u, v, w in roads:
        adj[u].append((v, w))
        adj[v].append((u, w))

    # priority queue:(distance, node)
    pq = [(0, 0)]
    dist = [float('inf')] * n
    ways = [0] * n

    dist[0] = 0
    ways[0] = 1
    mod = 10**9 + 7

    while pq:
        dis, node = heapq.heappop(pq)

        for v, W in adj[node]:
            if dis + W < dist[v]:
                dist[v] = dis + W
                ways[v] = ways[node] # impo
                heapq.heappush(pq, (dist[v], v))

            elif dis + W == dist[v]:
                ways[v] = (ways[v] + ways[node]) % mod

    return ways[n - 1] % mod

# Driver code
if __name__ == "__main__":
    n = 7
    edges = [
        [0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3],
        [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]
    ]

    ans = countPaths(n, edges)
    print(ans)























