# BOJ 1541, 잃어버린 괄호
import sys
from collections import deque
input = sys.stdin.readline

def make_num(stack):
    res = 0
    pos = 1
    while stack:
        cur_num = int(stack.pop())
        res += cur_num * pos
        pos = pos * 10
    return res

arr = deque(list(input().rstrip()))
not_num = ['-', '+']
is_negative = False

result = 0
while arr:
    target = arr.popleft()

    if target == '-':
        is_negative = True
        continue

    if target == '+':
        continue

    # 숫자일때
    num_stack = [target]

    # arr가 비어있게 될 경우 해당 숫자를 넣고 끝
    if not arr:
        if is_negative:
            result -= int(target)
        else:
            result += int(target)
        break

    while arr and arr[0] not in not_num:
        num_stack.append(arr.popleft())

    # 지금까지 num_queue에 들어간 숫자들을 꺼내면서 수로 만드는 함수
    cur_res = make_num(num_stack)

    # 음수 부호가 나온 이후라면 지금까지 나온 숫자들 모두 음의 부호로 합쳐주면 됨
    if is_negative:
        result -= cur_res
    else:
        result += cur_res

print(result)
# 35:00