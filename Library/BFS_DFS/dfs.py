
def dfs(graph, cur_node, visited):
    # 방문 처리
    visited[cur_node] = True

    # 방문 출력
    # print(cur_node, end=' ')

    for node in graph[cur_node]:
        if not visited[node]:
            # 방문하지 않은 해당 노드를 현재 노드로 dfs 재귀 호출
            dfs(graph, node, visited)

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

dfs(graph, 1, visited)
