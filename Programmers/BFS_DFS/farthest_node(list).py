# 프로그래머스, 가장 먼 노드 (시간 초과)

from collections import deque

def bfs(graph, start_node, visited):
    visited[start_node - 1] = 0
    queue = deque([start_node])

    while (queue):
        target_node = queue.popleft()

        target_level = visited[target_node - 1]
        target_level += 1

        for vertex in graph:

            if vertex[0] == target_node and visited[vertex[1] - 1] == -1:
                queue.append(vertex[1])
                visited[vertex[1] - 1] = target_level
            elif vertex[1] == target_node and visited[vertex[0] - 1] == -1:
                queue.append(vertex[0])
                visited[vertex[0] - 1] = target_level

    return visited  # 노드들의 거리를 가지고 있는 리스트


def solution(n, edge):
    cnt_lst = [-1] * n

    answer = bfs(edge, 1, cnt_lst)

    # 가장 긴 거리를 가지고 있는 노드의 갯수를 구하는 과정
    max_val = max(answer)
    cnt = answer.count(max_val)

    return cnt