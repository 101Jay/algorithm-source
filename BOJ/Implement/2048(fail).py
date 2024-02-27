# BOJ 12100, 2048(Easy)
import sys, copy
from itertools import product
N_INF = int(1e9) * -1
input = sys.stdin.readline

def move_map(arr, direct, n):

    if direct == 1: # 위쪽으로 이동
        # 모든 열을 순회하며 최상단 행으로 끌어올림
        for i in range(n):
            # 해당 열의 모든 행을 돌며 최대한 위로 올림 (0번째 행은 가장 위쪽이라 고려 x)
            success_sum = False
            for j in range(1, n):

                # 해당 숫자가 0이라면 확인할 필요없음
                if arr[j][i] == 0:
                    success_sum = False
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

                # 만약 위에가 없어서 j가 -1이 되었다면, 가장 위에 해당 숫자를 올림
                if j == -1:
                    arr[0][i] = target
                    success_sum = False
                    continue

                # 만약 위에 다른 숫자가 있다면, 해당 숫자와 같은지 확인
                if arr[j][i] == target and not success_sum:
                    arr[j][i] = target * 2
                    success_sum = True
                # 같지 않다면, 바로 직전 자리에 배치
                else:
                    arr[j+1][i] = target
                    success_sum = False

    elif direct == 2:  # 오른쪽으로 이동
        # 모든 행을 순회하며 가장 오른쪽 열로 밀어버림
        for i in range(n):
            # 해당 행의 모든 열을 돌며 최대한 오른쪽으로 밀어버림 (가장 오른쪽 행은 볼 필요 없음)
            success_sum = False
            for j in range(n-2, -1, -1):
                # 해당 숫자가 0이라면 확인할 필요없음
                if arr[i][j] == 0:
                    success_sum = False
                    continue

                # 해당 숫자 저장
                target = arr[i][j]
                arr[i][j] = 0

                # 바로 오른쪽에 다른 숫자가 있을 때까지 찾음
                j += 1
                while j < n:
                    if arr[i][j] != 0:
                        break
                    j += 1

                # 만약 옆에가 없어서 j가 n이 되었다면, 가장 위에 해당 숫자를 올림
                if j == n:
                    arr[i][n-1] = target
                    success_sum = False
                    continue

                # 만약 옆에 다른 숫자가 있다면, 해당 숫자와 같은지 확인
                if arr[i][j] == target and not success_sum:
                    arr[i][j] = target * 2
                    success_sum = True
                # 합칠 수 없다면, 바로 직전 자리에 배치
                else:
                    arr[i][j-1] = target
                    success_sum = False

    elif direct == 3: # 아래쪽으로 이동
        # 모든 열을 순회하며 최하단 행으로 끌어올림
        for i in range(n):
            # 해당 열의 모든 행을 돌며 최대한 위로 올림
            success_sum = False
            for j in range(n-2, -1, -1):

                # 해당 숫자가 0이라면 확인할 필요없음
                if arr[j][i] == 0:
                    success_sum = False
                    continue

                # 해당 숫자 저장
                target = arr[j][i]
                arr[j][i] = 0

                # 바로 아래쪽에 다른 숫자가 있을 때까지 찾음
                j += 1
                while j < n:
                    if arr[j][i] != 0:
                        break
                    j += 1

                # 만약 위에가 없어서 j가 n이 되었다면, 가장 아래에 해당 숫자를 올림
                if j == n:
                    arr[n-1][i] = target
                    success_sum = False
                    continue

                # 만약 위에 다른 숫자가 있다면, 해당 숫자와 같은지, 그리고 연속된 합은 아닌지 확인
                if arr[j][i] == target and not success_sum:
                    arr[j][i] = target * 2
                    success_sum = True
                # 같지 않다면, 바로 직전 자리에 배치
                else:
                    arr[j-1][i] = target
                    success_sum = False

    else:  # 왼쪽으로 이동
        # 모든 행을 순회하며 가장 왼쪽 열로 밀어버림
        for i in range(n):
            # 해당 행의 모든 열을 돌며 최대한 왼쪽으로 밀어버림
            success_sum = False
            for j in range(1, n):
                # 해당 숫자가 0이라면 확인할 필요없음
                if arr[i][j] == 0:
                    success_sum = False
                    continue

                # 해당 숫자 저장
                target = arr[i][j]
                arr[i][j] = 0

                # 바로 왼쪽에 다른 숫자가 있을 때까지 찾음
                j -= 1
                while j >= 0:
                    if arr[i][j] != 0:
                        break
                    j -= 1

                # 만약 옆에가 없어서 j가 n이 되었다면, 가장 왼쪽에 해당 숫자를 올림
                if j == -1:
                    arr[i][0] = target
                    success_sum = False
                    continue

                # 만약 옆에 다른 숫자가 있다면, 해당 숫자와 같은지 확인
                if arr[i][j] == target and not success_sum:
                    arr[i][j] = target * 2
                    success_sum = True
                # 같지 않다면, 바로 직전 자리에 배치
                else:
                    success_sum = False
                    arr[i][j+1] = target

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

    # print(step, copy_map)
    # step 속 다섯번의 이동을 순차적으로 순회
    for s in step:
        move_map(copy_map, s, n)
        # print(s, copy_map)

    # 이동 후, 블록의 최댓값을 구함
    for row in copy_map:
        tg = max(row)
        if tg > max_val:
            max_val = tg

print(max_val)