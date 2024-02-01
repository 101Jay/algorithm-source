# BOJ 18310, 안테나
import sys

# 타겟 인덱스로부터 좌 / 우측의 모든 데이터를 더한 결과를 리턴하는 함수
def path_len(arr, target_index, left):
    sum = 0
    if left:
        for i in range(target_index + 1):
            sum += arr[i]
    else:
        for i in range(1, target_index + 1):
            sum += arr[-i]

    return sum

input = sys.stdin.readline

num = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

arr.sort()

answer = 0
if num % 2 == 0:
    
    # 타겟 인덱스
    left_target = num // 2 - 1
    right_target = left_target + 1

    # 타겟 인덱스로부터 좌/우 거리의 총합
    left_sum = path_len(arr, left_target, True)
    right_sum = path_len(arr, right_target, False)
    
    # 타겟 인덱스로부터 좌/우 끝 위치까지의 거리가 더 작은 것을 답으로 선정
    if left_sum <= right_sum:
        answer = left_target
    else:
        answer = right_target
else:
    # 홀수 개수의 데이터의 경우 가운데 인덱스를 정답으로 산출
    answer = num // 2

print(arr[answer])