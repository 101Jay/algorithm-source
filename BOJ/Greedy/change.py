# BOJ 14916, 거스름돈
# 그리디

import sys

input = sys.stdin.readline
size = int(input())

five = size // 5

while(True):
    remainder = size - five * 5
    if(remainder % 2 != 0):

        # 2로 안 나누어 떨어지는 상황에서 five가 0이라면 -> 1을 출력
        if (five == 0):
            result = -1
            break

        # five가 0이 아니라면 -> five를 1 감소시키고 반복
        five -= 1
    else:
        # 2로 나누어 떨어진다면
        two = remainder // 2
        result = five + two
        break

print(result)