# 5 6
# 1 2 10
# 1 3 20
# 2 4 30
# 3 4 40
# 3 5 50
# 4 5 60
# matrix  

n, m = map(int, input().split())

adj = [ [0]*(n + 1) for _ in range(n + 1)]

# Input the edges
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u][v] = w
    adj[v][u] = w  # Remove this line for a directed graph


print(adj)

# op 
[ [0, 0, 0, 0, 0, 0], 
  [0, 0, 10, 20, 0, 0],
  [0, 10, 0, 0, 30, 0],
  [0, 20, 0, 0, 40, 50],
  [0, 0, 30, 40, 0, 60], 
  [0, 0, 0, 50, 60, 0]]
