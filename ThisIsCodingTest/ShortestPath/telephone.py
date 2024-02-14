# p262, 전보
'''
C에서 다른 연결된 모든 노드로 출발
C에서 보낸 메시지를 받게되는 도시의 개수를 출력

C를 시작점으로 하여 각 도시로 가는 거리가 INF가 아닌 도시들의 개수와 해당 도시로 가는 거리의 총합을 구하면 됨
n의 최댓값이 30000임으로 효율적인 다익스트라 알고리즘을 활용해야 함
'''
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

# 도시, 통로, 시작점 입력
n, m, c = map(int, input().rstrip().split())

# 각 노드들의 연결 관계를 저장할 graph
graph = [[] for _ in range(n+1)]

# 거리 정보를 저장할 distance 할당 및 INF로 초기화
distance = [INF] * (n+1)

# 간선들의 정보 입력 받기
for _ in range(m):
    # x -> y로 가는 비용 z
    x, y, z = map(int, input().rstrip().split())
    graph[x].append((y, z))

# dijkstra 알고리즘
def dijkstra(start):
    queue = []

    # 시작점인 c로 가는 거리는 0으로
    # heapq 라이브러리는 튜플이 들어왔을 때 첫 번째 원소로 가치를 매김으로 (거리, 노드) 형태로 저장
    heapq.heappush(queue, (0, c))

    # 시작 노드의 최단 거리 0으로 설정
    distance[c] = 0

    while queue:
        # 거리가 가장 짧은 노드
        tg_dist, tg_node = heapq.heappop(queue)

        # distance 속 최단 거리가 더 크다면, 이미 방문한 노드로 여기고 pass
        if distance[tg_node] < tg_dist:
            continue

        for node, dist in graph[tg_node]:
            # 현재 노드까지의 거리 + 해당 노드로 가는 거리
            cost = tg_dist + dist

            # cost가 기존의 거리보다 작으면 업데이트, queue에 넣어줌
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(queue, (cost, node))

dijkstra(c)

cnt = 0
max_val = 0
for i in range(1, n+1):
    if i == c:
        continue

    if distance[i] != INF:
        cnt += 1
        if distance[i] > max_val:
            max_val = distance[i]

print(cnt, max_val)

'''
입력 예시
3 2 1
1 2 4
1 3 2
---
출력 : 2 4
'''