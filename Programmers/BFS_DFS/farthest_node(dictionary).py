# 프로그래머스, 가장 먼 노드

from collections import deque

def bfs(graph, start_node, visited):
    visited[start_node - 1] = 0
    queue = deque([start_node])

    while (queue):
        target_node = queue.popleft()

        target_level = visited[target_node - 1]
        target_level += 1

        if target_node not in graph:
            continue

        tnode_list = graph[target_node]

        for node in tnode_list:

            if visited[node - 1] == -1:
                queue.append(node)
                visited[node - 1] = target_level

    return visited  # 노드들의 거리를 가지고 있는 리스트


def solution(n, edge):
    cnt_lst = [-1] * n

    # edge를 dictionary로 변경
    edge_dict = {}
    for e in edge:
        e1, e2 = e
        if e1 not in edge_dict:
            edge_dict[e1] = []
        if e2 not in edge_dict:
            edge_dict[e2] = []

        edge_dict[e1].append(e2)
        edge_dict[e2].append(e1)

    answer = bfs(edge_dict, 1, cnt_lst)

    # 가장 긴 거리를 가지고 있는 노드의 갯수를 구하는 과정
    max_val = max(answer)
    cnt = answer.count(max_val)

    return cnt

'''
사전 자료형은 내부적으로 해시 테이블을 이용함으로 검색 및 수정에 있어서 O(1)의 시간 복잡도를 갖는다.
즉, 특정 값들을 검색해야 한다면 dictionary를 사용하는 것이 훨씬 효율적이다.
'''