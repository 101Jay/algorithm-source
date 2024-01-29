# BOJ 1026, 보물

import sys
import heapq
input = sys.stdin.readline

num = int(input().strip())

array_a = list(map(int, input().split()))
heapq.heapify(array_a)

array_b = list(map(int, input().split()))
array_b.sort(reverse=True)

result = 0
for i in range(num):
    result += array_b[i] * heapq.heappop(array_a)

print(result)