# p96, 숫자 카드 게임
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

max_val = 0
for a in arr:

    min_val = min(a)

    # 해당 행을 대표하는 min_val과 max_val 비교하여 가장 큰 숫자를 업데이트
    max_val = max(max_val, min_val)

print(max_val)


'''
3 3
3 1 2
4 1 4
2 2 2
---
answer : 2

2 4
7 3 1 8
3 3 3 4
---
answer : 3
'''