# p153, 미로 탈출

import sys
import copy
input = sys.stdin.readline

def dfs(graph, cur_node, visited, count, n, m):

    count += 1
    i, j = cur_node
    # print(i, j, count)

    if i == n-1 and j == m-1:
        return count

    visited[i][j] = True

    steps = [
        (-1, 0), # 상
        (1, 0),  # 하
        (0, -1), # 좌
        (0, 1),  # 우
    ]

    min_cnt = 100000 # over 200 * 200

    cp_visited = copy.deepcopy(visited)
    for step in steps:
        cur_x = i + step[0]
        cur_y = j + step[1]

        if cur_x < 0 or cur_x >= n or cur_y < 0 or cur_y >= m:
            continue

        if not cp_visited[cur_x][cur_y] and graph[cur_x][cur_y] == 1:

            temp_cnt = dfs(graph, (cur_x, cur_y), cp_visited, 0, n, m)
            if temp_cnt < min_cnt:
                min_cnt = temp_cnt

    return min_cnt + count

n, m = map(int, input().rstrip().split())

maze = []
for i in range(n):
    # int 형태로 저장 -> 조금 더 보완이 필요해보임
    maze.append(list(map(int, list(input().rstrip()))))

check = [[False] * m for _ in range(n)]

min_path = dfs(maze, (0,0), check, 0, n, m)

print(min_path)


'''
5 6
101010
111111
000001
111111
111111
---
answer = 10

min_cnt를 초기에 100000이라는 접근할 수 없는 숫자로 설정
이에 따라, 만약 목적지(N,M)에 도착할 수 없는 경우, 100000에 count를 더한 값을 떠안기 때문에 최솟값이 될 수 없음
또한 목적지에 도착할 수 있다고 해도, 최적의 경로가 아닐 경우 min_cnt가 더 클 수 밖에 없기 때문에 정답이 될 수 없음
따라서 최적의 경로를 구할 수 있음

문제점
- visited 배열을 같은 것으로 순회할 경우, 이미 방문 처리한 노드들이 다음 순회에 영향을 미치기 때문에 제대로 된 정답이 나올 수 없음
- 따라서 visited를 deepcopy하여 순회시마다 다른 배열을 사용하도록 함
- 이렇게 하면, 최악의 경우 모든 노드 200 * 200 = 40000에 대해 200 * 200의 배열을 메모리에서 사용하게 됨
- 이는 40000 * 40000 = 1,600,000,000 (16억)의 메모리를 사용하게 되는 것임으로, 메모리 초과


-----
BFS를 활용할 경우 비교적 쉽게 문제가 풀림
- BFS는 같은 레벨의 노드에 대해서 count를 한 번씩 해나갈 수 있음
- 또한 같은 레벨의 노드 중 하나라도 목적지에 도착하면 해당 레벨에서 종료시킬 수 있음으로 이에 따라 최소의 경로를 count 할 수 있음
'''