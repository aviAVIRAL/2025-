# 5 6  
# n=no. of nodes  ||  m=tatal edges
# 1 2
# 1 3
# 2 4
# 3 4
# 3 5
# 4 5 

# matrix  

n, m = map(int, input().split())

adj = [ [0]*(n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u][v] = 1
    adj[v][u] = 1  # Remove this line for a directed graph


# ................................   
print(adj)

adj  = [ [0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 0, 0], 
         [0, 1, 0, 0, 1, 0], 
         [0, 1, 0, 0, 1, 1], 
         [0, 0, 1, 1, 0, 1], 
         [0, 0, 0, 1, 1, 0] ]

# .................................
# print(adj)
# for x in adj: 
#     print(*x)
# print()

# op rep  

# 0 0 0 0 0 0
# 0 0 1 1 0 0
# 0 1 0 0 1 0
# 0 1 0 0 1 1
# 0 0 1 1 0 1
# 0 0 0 1 1 0

