# BOJ 15686, 치킨 배달
import sys
from itertools import combinations
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().rstrip().split())
arr = []

for _ in range(n):
    row_data = list(map(int, input().rstrip().split()))
    arr.append(row_data)

home_arr = []
chicken_arr = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home_arr.append((i, j))
        elif arr[i][j] == 2:
            chicken_arr.append((i, j))

# 치킨 집 중, 살릴 M개의 조합 생성
alive_chicken = list(combinations(chicken_arr, m))

# 각 조합들을 돌면서, 해당 치킨 집만을 남긴 뒤 도시의 치킨 거리를 구한 뒤 이의 최소 값을 구하는 과정
min_total_cost = INF
for comb in alive_chicken:
    # 모든 집을 순회
    total_cost = 0
    for home in home_arr:
        home_x, home_y = home

        # 치킨거리를 담은 min_value
        min_value = INF

        # 치킨거리를 구하는 과정
        for chicken in comb:
            chicken_x, chicken_y = chicken
            cost = abs(home_x - chicken_x) + abs(home_y - chicken_y)
            if cost < min_value:
                min_value = cost

        # 도시 전체의 치킨거리를 구하기 위해 더해 줌
        total_cost += min_value

    # 해당 조합을 통해 구한 도시 전체 치킨거리가 가장 작은지 확인
    if total_cost < min_total_cost:
        min_total_cost = total_cost

print(min_total_cost)