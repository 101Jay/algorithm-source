# p149, 음료수 얼려먹기

import sys
input = sys.stdin.readline

def dfs(graph, cur_tup, visited, length, width):
    i, j = cur_tup

    # 방문 처리
    visited[i][j] = True

    # 갈 수 있는 곳은 상하좌우
    steps = [(-1,0), (1,0), (0,1), (0,-1)]

    # graph를 살펴 보며 갈 수 있는 곳 중 아직 안 간 곳으로 재귀함수 호출
    for step in steps:
        cur_x = i + step[0]
        cur_y = j + step[1]

        # graph out of index check
        if cur_x < 0 or cur_x >= length or cur_y < 0 or cur_y >= width:
            continue

        # 0인데 아직 방문되어 있지 않은 곳은 방문
        if graph[cur_x][cur_y] == 0 and not visited[cur_x][cur_y]:
            dfs(graph, (cur_x, cur_y), visited, length, width)


# length, width = list(map(int, input().rstrip().split()))
length, width = map(int, input().rstrip().split())
ices = []

for i in range(length):
    # 문자열을 리스트 형태로 변환
    # ices.append(list(input().rstrip()))
    ices.append(list(map(int, input().rstrip())))

# check 여부를 확인하기 위한 배열 초기화
check = [[False] * width for _ in range(length)]

# dfs를 한 번 탐색할 때마다 1씩 증가시킬 아이스크림
icecream = 0
for i in range(length):
    for j in range(width):

        # 방문하지 않은 것들 중, 원소가 0일 경우만 탐색
        if not check[i][j] and ices[i][j] == 0:
            icecream += 1
            dfs(ices, (i, j), check, length, width)

print(icecream)

'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
---
ans = 8

4 5
00110
00011
11111
00000
---
ans = 3
'''