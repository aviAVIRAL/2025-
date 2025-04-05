


# ...............undired graph ......................

# Dijkstra’s Algorithm 

import heapq

def dijkstra(V, adj, Sour):
    # Min-heap (priority queue) to store (distToance, node)
    pq = []
    heapq.heappush(pq, (0, Sour))
# ------------impo - --   
    # Initialize distToances with a large number
    dist = [float('inf')] * V
    dist[Sour] = 0
         
    while pq:
        Curr_dis, node = heapq.heappop(pq)
            
        for ngr, W in adj[node]:
            if Curr_dis + W < dist[ngr]:
                dist[ngr] = Curr_dis + W
                heapq.heappush(pq, (dist[ngr], ngr))
    return dist
# Driver code
V, E, S = 3, 3, 2

adj = [ [(1, 1), (2, 6)],  [(2, 3), (0, 1)],  [(1, 3), (0, 6)] ]

res = dijkstra(V, adj, S)
print(" ".join(map(str, res)))


# ...............undired graph ......................

adj = [ 
    [(1, 1), (2, 6)],  # node 0 is connected to 1 with weight 1, and to 2 with weight 6
    [(2, 3), (0, 1)],  # node 1 is connected to 2 with weight 3, and to 0 with weight 1
    [(1, 3), (0, 6)]   # node 2 is connected to 1 with weight 3, and to 0 with weight 6
]

# direct adj list given hai  

edges = [(0, 1, 1), (0, 2, 6), (1, 2, 3)]

# if edges given ho thi tu hum 
# convet kr te edges ko into 
# adj list mein 








