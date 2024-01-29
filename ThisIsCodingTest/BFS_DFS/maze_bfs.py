# p153, 미로 탈출

import sys
from collections import deque

def bfs(graph, start_node, visited, n, m):
    # graph나 visited, n, m 같은 것들은 전역 변수에서 그대로 끌고 올 수도 있긴 함
    # 그러나 함수의 독립성 및 재사용성을 위해 이와 같이 구현
    x, y = start_node
    visited[x][y] = 1
    queue = deque([start_node])

    steps = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while(queue):
        cur_node = queue.popleft()
        cur_x, cur_y = cur_node

        # 한 번의 순회
        reach_final = False
        for step in steps:
            mv_x = cur_x + step[0]
            mv_y = cur_y + step[1]

            # graph의 끝에 도달했으면 종료 조건은 True로 변경
            if mv_x == n-1 and mv_y == m-1:
                reach_final = True

            # graph의 인덱스 범위를 안 넘는지 체크
            if mv_x < 0 or mv_x >= n or mv_y < 0 or mv_y >= m:
                continue

            if visited[mv_x][mv_y] == -1 and graph[mv_x][mv_y] == 1:
                queue.append((mv_x, mv_y))
                visited[mv_x][mv_y] = visited[cur_x][cur_y] + 1

        if reach_final:
            break

    return visited

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

maze = []
for _ in range(n):
    # 문자열을 map 함수에 넣으면 한 글자 한 글자를 원소로 인식하여 반복
    maze.append(list(map(int, input().rstrip())))

check = [[-1] * m for _ in range(n)]

min_check = bfs(maze, (0,0), check, n, m)
print(min_check[n-1][m-1])


'''
5 6
101010
111111
000001
111111
111111
---
answer = 10
'''