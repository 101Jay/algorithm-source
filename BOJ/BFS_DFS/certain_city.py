# BOJ 18352, 특정 거리의 도시 찾기
import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, visited, cur_node):

    visited[cur_node - 1] = 0
    queue = deque([cur_node - 1])

    while queue:
        c_node = queue.popleft()
        if c_node not in graph:
            continue
        nodes = graph[c_node]

        for node in nodes:
            target_node = node # 이미 graph에 인덱스 형태로 들어가 있기에 그대로 쓰면 됨

            # 방문한 적이 없는 노드라면
            if visited[target_node] == -1:
                # 현재 노드의 거리에 1을 증가시킨 값을 저장
                visited[target_node] = visited[c_node] + 1
                queue.append(target_node)
            # 방문한 적이 있는 노드라면
            else:
                if visited[target_node] > visited[c_node] + 1:
                    # 최단거리가 아니라면 업데이트
                    # 아마 이런일은 없을 듯
                    visited[target_node] = visited[c_node] + 1

n, m, k, x = map(int, input().rstrip().split())

# road 정보 (= 그래프 정보)를 dictionary 형태로 저장 key는 노드 숫자, value는 해당 노드와 연결된 노드들의 리스트
roads = {}
for _ in range(m):
    start, end = map(int, input().rstrip().split())
    # 변환 과정에서 index로 변경
    if (start - 1) not in roads:
        roads[start - 1] = []
    roads[start - 1].append(end - 1)

visited = [-1] * n
bfs(roads, visited, x)

result = []
for i, node in enumerate(visited):
    if i+1 == x:
        # 출발도시는 최단 거리가 항상 0이기 때문에 어떠한 경우에도 출력에 포함 x
        continue
    # print(i+1, node)
    if node == k:
        result.append(i+1) # 인덱스가 아닌 번호 형태로 저장

result.sort()
if result:
    for res in result:
        print(res)
else:
    print(-1)