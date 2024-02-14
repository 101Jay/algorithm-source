# BOJ 14425, 문자열 집합
import sys
from bisect import bisect_right, bisect_left
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = []
for _ in range(n):
    arr.append(input().rstrip())

arr.sort()

result = []
for _ in range(m):
    target = input().rstrip()
    if bisect_left(arr, target) != bisect_right(arr, target):
        # 같지 않다는 건, 해당 원소가 arr에 존재한다는 것
        result.append(target)

print(len(result))