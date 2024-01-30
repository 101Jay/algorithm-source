# BOJ 1439, 뒤집기
import sys

def reverse_coin(str, change, cnt):
    before = str[0]

    for i, ch in enumerate(str):

        if ch == before:
            # 앞선 것과 같다면 뒤집을 필요가 없음

            if i != 0:
                # 첫 번째 원소가 아닐 경우에만 False로 설정 (첫 동전을 뒤집는 경우를 위해)
                change = False
        else:
            # 앞선 것과 같지 않다면 cnt 증가, 단 연속된 변화가 아닐 때만
            if not change:
                cnt += 1

                # 이후의 변화는 연속된 변화
                change = True

    return cnt

input = sys.stdin.readline
str = list(map(int, list(input().rstrip())))

# 1. 첫 번째 연속된 동전을 뒤집지 않는 경우 (그대로)
not_rev = reverse_coin(str, False, 0)

# 2. 첫 번째 연속된 동전을 뒤집는 경우
if str[0] == 0:
    str[0] = 1
else:
    str[0] = 0

# 첫 번째 동전을 뒤집은 경우임으로 cnt를 1로 초기화
rev = reverse_coin(str, True, 1)

print(min(not_rev, rev))