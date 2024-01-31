# BOJ 2110, 공유기 설치
import sys

def install_wifi(gap, arr, wifi_num):
    cur_house = arr[0]
    cnt = 1
    # 첫 번째 집에 와이파이를 설치했다고 가정하고, 주어진 간격으로 wifi를 몇 개나 설치할 수 있을지 확인
    for house in arr:
        if house >= cur_house + gap:
            cnt += 1
            cur_house = house

    if cnt >= wifi_num:
        return True

    return False

input = sys.stdin.readline
n, c = map(int, input().rstrip().split())
home = [int(input().rstrip()) for _ in range(n)]

# 이진탐색을 위한 정렬
home.sort()

start, end = 1, home[-1] - home[0]
max_gap = 0
while start <= end:
    mid = (start + end) // 2

    if install_wifi(mid, home, c):
        # 해당 gap으로 wifi를 모두 설치할 수 있다면, 해당 결과를 저장한 뒤 gap을 넓혀서 탐색
        start = mid + 1
        max_gap = mid
    else:
        # 해당 gap으로 wifi를 모두 설치할 수 없다면, gap을 좁혀서 탐색
        end = mid - 1

print(max_gap)