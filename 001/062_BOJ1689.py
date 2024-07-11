import sys, heapq

input = sys.stdin.readline
n = int(input())
array = [tuple(map(int, input().split())) for _ in range(n)]
array.sort(key=lambda x: x[0])
min_heap = []
heapq.heappush(min_heap, array[0][1])
result = 1
for x in array[1:]:
    while min_heap and min_heap[0] <= x[0]:
        heapq.heappop(min_heap)
    heapq.heappush(min_heap, x[1])
    result = max(result, len(min_heap))

print(result)
