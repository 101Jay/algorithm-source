# BOJ 1916, 최소비용 구하기
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input().rstrip())
m = int(input().rstrip())

# 그래프 간의 이동 거리를 표현할 인접 행렬 graph[해당 노드] = [(목적지 노드, 거리), ...]
graph = [[] for _ in range(n+1)]

# 그래프 간의 최소거리를 나타낼 리스트
distance = [INF] * (n+1)

for _ in range(m):
    start, end, cost = map(int, input().rstrip().split())
    graph[start].append((end, cost))

start_node, dest_node = map(int, input().rstrip().split())

def dijkstra(start):
    queue = []
    # 힙 큐에는 시작 노드로부터의 (거리, 노드) 식으로 저장하여, 거리가 가장 짧은 것을 우선 pop할 수 있도록 함
    heapq.heappush(queue, (0, start))

    # 시작노드에서 시작노드로의 거리는 0으로 초기화
    distance[start] = 0

    while queue:
        # 갈 수 있는 곳들 중 가장 작은 것을 pop
        tg_dist, tg_node = heapq.heappop(queue)

        # 최소거리가 더 짧다면 이미 방문한 노드임으로 건너뜀 (로직상 중복되어 큐에 들어갈 수 있기 때문)
        if distance[tg_node] < tg_dist:
            continue

        for node, dist in graph[tg_node]:
            # tg_node를 거쳐서 node로 가는 비용 계산
            cost = tg_dist + dist

            # 해당 비용이 start -> node로 가는 최소비용이라면 업데이트
            if cost < distance[node]:
                distance[node] = cost
                # queue에 해당 위치를 (거리, 노드) 형태로 저장
                heapq.heappush(queue, (cost, node))

dijkstra(start_node)
# 반드시 도착 가능한 경우만 주어짐으로 별도 예외처리 X
print(distance[dest_node])