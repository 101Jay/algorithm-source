from collections import deque

def bfs(graph, start_node, visited):
    # 시작 노드 방문 처리
    visited[start_node] = True

    # start_node를 넣은 queue 선언
    queue = deque([start_node])

    while(queue):
        # queue가 빌 때까지 반복
        cur_node = queue.popleft()
        print(cur_node, end=' ')

        for node in graph[cur_node]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)

graph = [
    [], # 0번 노드
    [2, 3, 8], # 1번 노드
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)