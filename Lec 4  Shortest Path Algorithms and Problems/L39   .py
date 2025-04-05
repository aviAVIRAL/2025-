


import heapq

nums = [5, 1, 9, 3]
max_heap = []

# Push negative values
for num in nums:
    heapq.heappush(max_heap, -num)

# Pop and convert back to positive
largest = -heapq.heappop(max_heap)
print(largest)  # Output: 9
