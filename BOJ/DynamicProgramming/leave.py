# BOJ 14501, 퇴사
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for _ in range(n):
    data = tuple(map(int, input().rstrip().split()))
    arr.append(data)

# 각 항에서 완료할 수 있는 일을 담은 리스트(최대 범위 20)
can_arr = [[] for _ in range(20)]

for i, tup in enumerate(arr):
    t, p = tup
    # 해당 일로부터 t를 더한 곳의 번호 위치에, 자신의 번호와 금액을 저장
    can_arr[i+t].append((i+1, p))

# 점화식의 결과를 저장해 나갈 res_arr
res_arr = [0 for _ in range(20)]

for j in range(1, n+1):
    # 해당 일에 마무리 할 수 있는 일 리스트 possible_lst
    possible_lst = can_arr[j]

    max_val = 0
    for p_tup in possible_lst:
        num, price = p_tup
        # 점화식 An => 모든 가능한 리스트를 돌며,
        # max(현재 위치에서 끝날 수 있는 일의 금액 + 해당하는 작업의 시작 일의 직전 일까지의 최대 금액)를 구함
        cost = res_arr[num-1] + price
        if max_val < cost:
            max_val = cost

    # 만약 max_val가 0이거나, 이전 항의 값보다 작다면, 이전 항의 값을 그대로 가져오는 것이 더 유리함
    if max_val < res_arr[j-1]:
        max_val = res_arr[j-1]

    res_arr[j] = max_val

print(res_arr[n])