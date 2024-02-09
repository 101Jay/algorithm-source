# BOJ 19637, IF문 좀 대신 써줘
import sys
from bisect import bisect_left
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
level_name = []
level_limit = []
for _ in range(n):
    name, num = input().rstrip().split()
    level_name.append(name)
    level_limit.append(int(num))

result = []
for _ in range(m):
    data = int(input().rstrip())
    index = bisect_left(level_limit, data)

    result.append(level_name[index])

for res in result:
    print(res)