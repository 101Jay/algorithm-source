# BOJ 5525, IOIOI
import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
string_size = int(input().rstrip())
str_data = deque(list(input().rstrip()))

result = 0
while str_data:
    ch = str_data.popleft()

    # O일 때는 건너뜀
    if ch == 'O':
        continue

    # ch가 I인 상황
    temp = 'I'

    cnt = 1
    # 서로 다른 문자가 나오는 것을 반복하며 I가 나오는 개수를 확인
    while str_data and str_data[0] != temp:
        data = str_data.popleft()
        if data == 'I':
            temp = 'I'
            cnt += 1
        else:
            temp = 'O'

    # I와 O가 연속적으로 반복되는 해당 부분 안에서 몇 개의 Pn이 나올 수 있을지 판단
    # ex) cnt = 5 -> IOIOIOIOI 임
    # n = 2라고 하면, 3개가 가능
    # 즉, cnt - n 해주면 됨

    # cnt - n이 0보다 작거나 같은 경우는 더해주면 안 됨
    if cnt > 1 and cnt - n > 0:
        result += (cnt - n)

print(result)