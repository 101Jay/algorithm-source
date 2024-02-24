# BOJ 20300, 서강근육맨
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
arr.sort()

queue = deque(arr)

max_val = -1
# 홀수라면, 가장 큰 수 하나를 제거
if n % 2 == 1:
    max_val = queue.pop()

# 가장 큰 수는, 가장 작은 수와 더해져야 함
while queue:
    bigger = queue.pop()
    smaller = queue.popleft()

    cost = bigger + smaller

    if max_val < cost:
        max_val = cost

print(max_val)