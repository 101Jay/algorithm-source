# BOJ 1012, 유기농 배추
import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

def dfs(arr, visited, cur_node, length, width):

    # 현재 노드 방문 처리
    cur_x, cur_y = cur_node
    visited[cur_x][cur_y] = True

    # 현재 노드에서 갈 수 있는 위치 파악
    steps = [
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0)
    ]

    for step in steps:
        x, y = step
        mv_x = cur_node[0] + x
        mv_y = cur_node[1] + y

        # index 범위를 벗어나지 않았는지 확인
        if mv_x < 0 or mv_x >= length or mv_y < 0 or mv_y >= width:
            continue
        # 아직 탐색하지 않았을 경우에만 탐색
        if not visited[mv_x][mv_y] and arr[mv_x][mv_y] == 1:
            dfs(arr, visited, (mv_x, mv_y), length, width)


tast_case = int(input().rstrip())

result = []
for _ in range(tast_case):

    n, m, k = map(int, input().rstrip().split())
    arr = [[0] * m for _ in range(n)]

    # 양배추 표시
    for _ in range(k):
        x, y = map(int, input().rstrip().split())
        arr[x][y] = 1

    # DFS를 통한 지역 수 확인
    visited = [[False] * m for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == 1:
                # 아직 방문하지 않았고, 양배추가 있다면 탐색
                dfs(arr, visited, (i, j), n, m)
                cnt += 1

    result.append(cnt)

# 결과 출력
for elem in result:
    print(elem)