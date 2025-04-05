
# 5 6
# 1 2
# 1 3
# 2 4
# 3 4
# 3 5
# 4 5

# edges gioven haio. 
# convert itno adjancy list 

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())  # u -> v
    adj[u].append(v)
    adj[v].append(u)

print(adj)
# op 
#    [ [], [2, 3], [1, 4], [1, 4, 5], [2, 3, 5], [3, 4] ]

# -------------  ----------------

# # Print the adjacency list for verification
# for i in range(1, n + 1):
#     print(f"Node {i}: {adj[i]}")

# # op  
# Node 1: [2, 3]
# Node 2: [1, 4]
# Node 3: [1, 4, 5]
# Node 4: [2, 3, 5]
# Node 5: [3, 4]
  

