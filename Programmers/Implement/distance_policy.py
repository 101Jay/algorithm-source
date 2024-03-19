# Programmers 81302, 거리두기 확인하기
from itertools import combinations
def solution(places):
    answer = []

    for place in places:
        # 사람 위치 저장하기
        people = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append((i, j))

        # 사람들간의 조합 구하기
        people_comb = list(combinations(people, 2))

        # 각 조합을 순회하며 거리두기를 지키고 있는지 확인
        is_right = True
        for comb in people_comb:
            p1, p2 = comb
            x1, y1 = p1
            x2, y2 = p2

            # 맨해튼 거리 구하기
            man_cost = abs(x1 - x2) + abs(y1 - y2)

            if man_cost >= 3:
                continue

            # 거리가 1이라면 붙어있는 것임으로 해당 place는 거리두기 안된 상태
            if man_cost == 1:
                is_right = False
                break

            # man_cost가 2라면
            # 두 위치가 같은 열이나 행에 있을 경우
            if x1 == x2:  # 같은 행에 있을 경우
                # 그 사이가 칸막이가 아니라면 break
                if place[x1][(y1 + y2) // 2] != 'X':
                    is_right = False
                    break
                continue

            if y1 == y2:  # 같은 열에 있을 경우
                if place[(x1 + x2) // 2][y1] != 'X':
                    is_right = False
                    break
                continue

            # 두 위치가 대각 방향에 있는 경우, 그 반대 대각 방향이 모두 칸막이여야 거리두기 하는 중
            # 두 가지 경우의 수
            if place[max(x1, x2)][min(y1, y2)] == 'X' and place[min(x1, x2)][max(y1, y2)] == 'X':
                continue
            elif place[max(x1, x2)][max(y1, y2)] == 'X' and place[min(x1, x2)][min(y1, y2)] == 'X':
                continue
            else:
                is_right = False
                break

        if is_right:
            answer.append(1)
        else:
            answer.append(0)

    return answer