# BOJ 14502, 연구소
import sys, copy
from itertools import combinations
input = sys.stdin.readline

def dfs(graph, visit, cur_node, n, m):
    x, y = cur_node
    visit[x][y] = True

    # 탐색하게 되는 빈칸이라면 바이러스 감염
    if graph[x][y] == 0:
        graph[x][y] = 2

    steps = [
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1)
    ]

    for step in steps:
        mv_x = x + step[0]
        mv_y = y + step[1]

        if mv_x < 0 or mv_x >= n or mv_y < 0 or mv_y >= m:
            # 그래프의 범위를 벗어나지 않도록
            continue

        if not visit[mv_x][mv_y] and graph[mv_x][mv_y] != 1:
            # 1이 아니라면 계속 탐색
            dfs(graph, visit, (mv_x, mv_y), n, m)


n, m = map(int, input().rstrip().split())

arr = []
for _ in range(n):
    line = list(map(int, input().rstrip().split()))
    arr.append(line)

# 빈칸만을 담은 리스트를 생성
empty_lst = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            empty_lst.append((i,j))

# 빈칸들 중 3개의 조합을 뽑는 조합 리스트 생성
comb_empty = list(combinations(empty_lst, 3))

max_safe = 0

# 각 빈칸 조합들을 순회하며, 각 순회마다 dfs 탐색을 수행하며 안전영역의 최댓값을 구한 뒤 갱신
for comb in comb_empty:
    t_arr = copy.deepcopy(arr)

    # 선택된 조합대로 벽 세우기
    for x, y in comb:
        t_arr[x][y] = 1

    visited = [[False] * m for _ in range(n)]
    # dfs 탐색 수행
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == 2:
                # 방문 안 한 바이러스가 존재할 경우에 탐색(값이 2일 때만)
                dfs(t_arr, visited, (i, j), n, m)


    # dfs 후, 안전영역의 개수 확인
    cnt = 0
    for h in range(n):
        for k in range(m):
            if t_arr[h][k] == 0:
                cnt += 1

    # 안전영역 최댓값 갱신
    if cnt > max_safe:
        max_safe = cnt

print(max_safe)