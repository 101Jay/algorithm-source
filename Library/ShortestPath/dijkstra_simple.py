# 간단한 구현 방식의 다익스트라 알고리즘
# 시간복잡도 : O(V^2), V는 노드의 개수
# V <= 5,000 정도면 활용 가능

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 10억

# 노드 및 간선의 개수
n, m = map(int, input().rstrip().split())

# 시작 노드
init_node = int(input().rstrip())

# 각 노드별로 연결된 노드들의 리스트를 저장하는 graph
graph = [[] for i in range(n+1)]

# 방문 체크를 위한 리스트
visited = [False] * (n+1)

# 최단 거리 테이블 -> 무한으로 초기화
distance = [INF] * (n+1)

# 간선 정보 입력
for _ in range(m):
    # a -> b로 가는 비용 c
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b,c))

# 방문하지 않은 노드들 중, 최단 거리의 노드를 선택
def get_smallest_node(dist, visit):
    min_value = INF
    min_index = 0 # 최단 거리 노드(인덱스) 저장
    for i in range(1, n+1):
        # 방문하지 않은 노드 중 최단 거리의 노드를 찾는 과정
        if dist[i] < min_value and not visit[i]:
            min_value = dist[i]
            min_index = i
    return min_index

# 다익스트라 알고리즘
def dijkstra(start):
    # 시작 노드 초기화
    visited[start] = True
    distance[start] = 0 # 시작 노드에 대한 거리는 0으로 설정
    for j in graph[start]:
        # start와 연결된 노드들을 방문하며 최단 거리 업데이트
        distance[j[0]] = j[1]

    # n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 방문하지 않은 노드 중 최단 거리의 노드를 찾는 함수
        target = get_smallest_node(distance, visited)

        # 최단 거리 노드 방문 처리
        visited[target] = True

        # 현재 노드와 연결된 다른 노드들의 최단 거리 업데이트
        for j in graph[target]:
            cost = distance[target] + j[1]
            # 해당 노드로 가는 거리가, 기존의 거리보다 현재 노드를 거쳐가는 것이 더 짧을 경우만 이동
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(init_node)

# 모든 노드로 가는 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우만 거리를 출력
    else:
        print(distance[i])

'''
입력 예시
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
---
출력 예시
0
2
3
1
2
4
'''