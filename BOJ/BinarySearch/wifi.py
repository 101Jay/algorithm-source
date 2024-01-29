# BOJ 2110
# 탐색 범위가 10억개, 집의 개수 20만개

import sys
input = sys.stdin.readline

house_num, wifi_num = map(int, input().rstrip().split())
house_arr = [int(input().rstrip()) for _ in range(house_num)]
house_arr.sort()

# 갭의 최소와 최대 범위를 저장
# 첫 번째 위치에는 반드시 공유기를 설치한다고 가정
# 첫 번재 위치를 기준으로 gap이 가장 작은 start와, gap이 가장 큰 end를 구함
# 무조건 최대한 멀리 띄어 놓아야 하기 때문에 첫 번째 위치에는 반드시 설치
# start = house_arr[1] - house_arr[0]
start = 1
end = house_arr[-1] - house_arr[0]
result = 0

while start <= end:
    # mid가 gap의 역할
    mid = (start + end) // 2

    cur_node = house_arr[0]
    # 첫 번째 위치에 공유기 하나를 설치
    wifi = 1
    for i in range(1, house_num):
        if house_arr[i] - cur_node >= mid:
            cur_node = house_arr[i]
            wifi += 1

    if wifi < wifi_num:
        # 공유기 개수가 충분하지 않다면 gap의 범위를 더 줄임
        end = mid - 1
    else:
        # 공유기 개수가 충분하다면 gap의 범위를 넓힘
        start = mid + 1
        # 최적의 결과를 저장
        result = mid

print(result)

'''
start = house_arr[1] - house_arr[0] 할 경우의 반례

3 3
1
9
10
---
출력 : 0
정답 : 1

탐색의 시작 범위는 1로 설정해줘야 함
'''