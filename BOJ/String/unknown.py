# BOJ 1764, 듣보잡
import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

n_arr = []
for _ in range(n):
    n_arr.append(input().rstrip())
# 이진 탐색을 위해 sorting
n_arr.sort()

result = []
for _ in range(m):
    target = input().rstrip()
    if bisect_left(n_arr, target) != bisect_right(n_arr, target):
        # 해당 값이 이미 존재한다는 것
        result.append(target)

print(len(result))
result.sort()

for res in result:
    print(res)

# 20:00