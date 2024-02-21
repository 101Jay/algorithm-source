# BOJ 14889, 스타트와 링크
import sys
from itertools import combinations
input = sys.stdin.readline
INF = int(1e9)

n = int(input().rstrip())
arr = []
for _ in range(n):
    row_data = list(map(int, input().rstrip().split()))
    arr.append(row_data)

player_arr = [x for x in range(1, n+1)]

# 스타트팀 조합 구하기
start_lst = list(combinations(player_arr, (n//2)))

min_diff = INF
# 스타트팀 조합을 순회
for start in start_lst:
    # 링크 팀 구하기
    link = []
    for player in player_arr:
        if player not in start:
            link.append(player)

    # 스타트팀 조합의 능력치 구하기
    start_cost = 0
    start_comb = list(combinations(start, 2))
    for s in start_comb:
        start_cost += arr[s[0]-1][s[1]-1]
        start_cost += arr[s[1]-1][s[0]-1]

    # 링크팀 조합의 능력치 구하기
    link_cost = 0
    link_comb = list(combinations(link, 2))
    for l in link_comb:
        link_cost += arr[l[0]-1][l[1]-1]
        link_cost += arr[l[1]-1][l[0]-1]

    dif = abs(start_cost - link_cost)
    if dif < min_diff:
        min_diff = dif

print(min_diff)