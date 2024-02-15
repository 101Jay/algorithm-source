# BOJ 1260, DFS와 BFS
import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().rstrip().split())
edges = {}

for _ in range(m):
    t1, t2 = map(int, input().rstrip().split())
    if t1 not in edges:
        edges[t1] = []
    if t2 not in edges:
        edges[t2] = []
    edges[t1].append(t2)
    edges[t2].append(t1)

# 중복되는 간선 정보를 제거, 정렬
# 각 키 값의 value들, 즉 노드들의 리스트를 꺼내, 중복 제거 및 정렬
for key, edge in edges.items():
    edge = list(set(edge))
    edge.sort()
    edges[key] = edge

dfs_check = deque([])
def dfs(graph, visit, cur_node):
    visit[cur_node] = True
    dfs_check.append(cur_node)

    if cur_node not in graph:
        return

    node_lst = graph[cur_node]

    for node in node_lst:
        if not visit[node]:
            dfs(graph, visit, node)

bfs_check = deque([])
def bfs(graph, visit, start):
    visit[start] = True
    bfs_check.append(start)

    queue = deque([start])
    while queue:
        target = queue.popleft()

        if target not in graph:
            continue
        node_lst = graph[target]

        for node in node_lst:
            if not visit[node]:
                visit[node] = True
                bfs_check.append(node)
                queue.append(node)

dfs_visit = [False] * (n+1)
dfs(edges, dfs_visit, v)

bfs_visit = [False] * (n+1)
bfs(edges, bfs_visit, v)

for t in dfs_check:
    print(t, end=' ')
print()
for b in bfs_check:
    print(b, end=' ')