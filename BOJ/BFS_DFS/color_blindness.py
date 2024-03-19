# BOJ 10026, 적록색약
import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def dfs(cur_node, visit, n, color):
    # 현재 노드 방문 처리
    x, y = cur_node
    visit[x][y] = True

    # 갈 수 있는 거리 정하기
    steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for step in steps:
        mv_x, mv_y = x + step[0], y + step[1]

        # 범위를 넘어서는지 확인
        if mv_x < 0 or mv_x >= n or mv_y < 0 or mv_y >= n:
            continue

        if arr[mv_x][mv_y] == color and not visit[mv_x][mv_y]:
            dfs((mv_x, mv_y), visit, n, color)


n = int(input().rstrip())
arr = []
for _ in range(n):
    row = list(input().rstrip())
    arr.append(row)

# 적록색맹이 아닌 경우 구역 구하기
visited = [[False] * (n) for _ in range(n)]

cnt1 = 0
for i in range(n):
    for j in range(n):
        # 아직 방문하지 않았다면 dfs 탐색 후 cnt 1 증가
        if not visited[i][j]:
            dfs((i, j), visited, n, arr[i][j])
            cnt1 += 1

# 적록색맹 환경 세팅
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

# 적록색맹인 경우 구역 구하기
visited = [[False] * (n) for _ in range(n)]

cnt2 = 0
for i in range(n):
    for j in range(n):
        # 아직 방문하지 않았다면 dfs 탐색 후 cnt 1 증가
        if not visited[i][j]:
            dfs((i, j), visited, n, arr[i][j])
            cnt2 += 1

print(cnt1, cnt2)