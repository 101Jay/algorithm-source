# Programmers 68936, 쿼드압축 후 개수 세기
import sys
sys.setrecursionlimit(2000000)

def solution(arr):
    answer = [0, 0]  # 모두 0개로 초기화
    size = len(arr)
    recur_sol((0, 0), (size - 1, size - 1), arr, answer)

    return answer

def recur_sol(start, end, arr, answer):
    x1, y1 = start
    x2, y2 = end

    # 해당 영역이 한 개의 셀로 이루어졌다면 해당 값 1 증가 후 탈출(초기 조건)
    if x1 == x2 and y1 == y2:
        answer[arr[x1][y1]] += 1
        return

    # 해당 영역의 모든 값이 동일한지 확인
    is_diff = False
    comp = arr[x1][y1]
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if arr[x][y] != comp:
                is_diff = True
                break

    # 해당 영역의 모든 값이 동일하다면 해당 값의 카운트를 1 증가
    if not is_diff:
        answer[comp] += 1
    else:
        # 동일하지 않다면 네 개의 정사각형으로 분할한 뒤 재귀
        recur_sol((x1, y1), ((x1 + x2) // 2, (y1 + y2) // 2), arr, answer)
        recur_sol((x1, (y1 + y2) // 2 + 1), ((x1 + x2) // 2, y2), arr, answer)
        recur_sol(((x1 + x2) // 2 + 1, y1), (x2, (y1 + y2) // 2), arr, answer)
        recur_sol(((x1 + x2) // 2 + 1, (y1 + y2) // 2 + 1), (x2, y2), arr, answer)