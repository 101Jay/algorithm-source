# 프로그래머스, 무인도 여행

import sys
# 파이썬의 기본 재귀 깊이 제한인 1000을 더 늘려줌
sys.setrecursionlimit(10000)

def dfs(graph, cur_node, visited, n, m, cnt):
    x, y = cur_node
    visited[x][y] = True
    cnt += int(graph[x][y])

    steps = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for step in steps:
        cur_x = x + step[0]
        cur_y = y + step[1]

        # map을 넘어가는지 체크
        if cur_x < 0 or cur_x >= n or cur_y < 0 or cur_y >= m:
            continue

        if not visited[cur_x][cur_y] and graph[cur_x][cur_y] != 'X':
            cnt = dfs(graph, (cur_x, cur_y), visited, n, m, cnt)

    return cnt


def solution(maps):
    answer = []
    maps_height = len(maps)
    maps_length = len(maps[0])

    check_lst = [[False] * maps_length for _ in range(maps_height)]

    for i in range(maps_height):
        for j in range(maps_length):
            if maps[i][j] != 'X' and not check_lst[i][j]:
                cur_cnt = dfs(maps, (i, j), check_lst, maps_height, maps_length, 0)
                answer.append(cur_cnt)

    answer.sort()
    if not answer:
        answer.append(-1)

    return answer