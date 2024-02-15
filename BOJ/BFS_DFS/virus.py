# BOJ 2606, 바이러스
# 1번 컴퓨터로부터 감염되게 되는 컴퓨터의 수를 출력
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
e = int(input().rstrip())
edge = {} # 해당 노드에 연결된 다른 노드들을 편하게 찾기 위해 dictionary로 설정

# 간선 정보 입력 받기
for _ in range(e):
    t1, t2 = map(int, input().rstrip().split())

    if t1 not in edge:
        edge[t1] = []
    if t2 not in edge:
        edge[t2] = []

    edge[t1].append(t2)
    edge[t2].append(t1)

def bfs(graph, visit, start):
    visit[start] = True

    queue = deque([start])
    while queue:
        target = queue.popleft()

        if target not in graph:
            continue

        node_lst = graph[target]

        for node in node_lst:
            if not visit[node]:
                visit[node] = True
                queue.append(node)

visited = [False] * (n+1)

bfs(edge, visited, 1)

cnt = 0
for i in range(2, n+1):
    if visited[i] == True:
        cnt += 1

print(cnt)