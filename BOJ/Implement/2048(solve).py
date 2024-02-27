# BOJ 12100, 2048(Easy)
import sys, copy
from itertools import product
N_INF = int(1e9) * -1
input = sys.stdin.readline

def rotate_map(arr, direct, n):
    new_map = copy.deepcopy(arr)

    if direct == 2:
        # 오른쪽 방향으로 회전
        for i in range(n):
            for j in range(n):
                new_map[j][n-1-i] = arr[i][j]
    elif direct == 4:
        # 왼쪽 방향으로 회전
        for i in range(n):
            for j in range(n):
                new_map[n-1-j][i] = arr[i][j]

    return new_map

def move_map(arr, n):
    # 모든 열을 순회하며 최상단 행으로 끌어올림
    for i in range(n):
        # 해당 열의 모든 행을 돌며 최대한 위로 올림 (0번째 행은 가장 위쪽이라 고려 x)
        success_sum = False
        for j in range(1, n):
            # 해당 숫자가 0이라면 확인할 필요없음
            if arr[j][i] == 0:
                continue

            # 해당 숫자 저장 후 해당 자리에는 0을 세팅
            target = arr[j][i]
            arr[j][i] = 0

            # 바로 위에 다른 숫자가 있을 때까지 찾음
            j -= 1
            while j >= 0:
                if arr[j][i] != 0:
                    break
                j -= 1

            # 만약 위에가 없어서 j가 -1이 되었다면, 가장 위에 해당 숫자를 올림(success_sum은 그대로)
            if j == -1:
                arr[0][i] = target
                continue

            # 만약 위에 다른 숫자가 있다면, 해당 숫자와 같은지, 그리고 연속되어 합쳐지는 것은 아닌지 확인
            if arr[j][i] == target and not success_sum:
                arr[j][i] = target * 2
                success_sum = True
            # 같지 않다면, 바로 직전 자리에 배치
            else:
                arr[j+1][i] = target
                success_sum = False


n = int(input().rstrip())
arr = []
for _ in range(n):
    row_data = list(map(int, input().rstrip().split()))
    arr.append(row_data)

steps = [1, 2, 3, 4] # 위, 오른쪽, 아래, 왼쪽
step_comb = list(product(steps, repeat=5))

max_val = N_INF
# 모든 이동 조합의 경우의 수를 순회
for step in step_comb:

    # 기존의 맵을 카피하여 수행
    copy_map = copy.deepcopy(arr)

    # step 속 다섯번의 이동을 순차적으로 순회
    for s in step:
        if s == 2:
            copy_map = rotate_map(copy_map, 4, n)
            move_map(copy_map, n)
            copy_map = rotate_map(copy_map, 2, n) # 원상복구
        elif s == 4:
            copy_map = rotate_map(copy_map, 2, n)
            move_map(copy_map, n)
            copy_map = rotate_map(copy_map, 4, n)  # 원상복구
        elif s == 3:
            copy_map = rotate_map(copy_map, 2, n)
            copy_map = rotate_map(copy_map, 2, n)
            move_map(copy_map, n)
            copy_map = rotate_map(copy_map, 2, n) # 원상복구
            copy_map = rotate_map(copy_map, 2, n) # 원상복구
        else:
            move_map(copy_map, n)

    # 이동 후, 블록의 최댓값을 구함
    for row in copy_map:
        tg = max(row)
        if tg > max_val:
            max_val = tg

print(max_val)