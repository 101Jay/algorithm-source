# 서로소 집합을 활용한 '무방향' 그래프에서의 사이클 찾기
'''
서로소 집합 찾기
- 각 간선 간의 연결을 확인하여 각 노드들의 루트 노드를 기록
- 각 루트 노드가 동일한 노드들은 동일한 서로소 집합에 속하는 것으로 판단

서로소 집합을 활용한 무방향 그래프에서의 사이클 찾기
- 간선 간의 연결을 통해 각 노드들의 루트 노드를 확인
- 만약 서로 다른 두 노드 간의 루트 노드가 동일하다면 사이클이 존재하는 것으로 판단
'''
import sys

# 특정 원소의 루트 노드 찾기
def find_parent(parent, x):
    # 루트 노드는 스스로를 부모로 가리키고 있는 노드
    # 루트 노드가 아니라면 재귀적으로 부모를 찾는 함수를 호출하여 루트 노드를 찾음
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# Union 함수 정의
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 기본적으로 더 작은 노드를 부모로 삼는 것을 원칙으로 함
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드, 간선의 개수 입력
v, e = map(int, input().rstrip().split())

# 부모 테이블 생성 및 자기 자신으로 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

cycle = False

# 반복적으로 간선들을 입력 받아 union 연산을 수행하며, 사이클 발생 여부 확인
for i in range(e):
    a, b = map(int, input().rstrip().split())

    # 싸이클이 발생한 경우
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 싸이클이 발생하지 않았다면 union 연산 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("Cycle is founded")
else:
    print("There is no cycle")

'''
입력 예시
3 3
1 2
1 3
2 3
--- 
출력 : Cycle is founded
'''