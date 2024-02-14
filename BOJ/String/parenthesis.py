# BOJ 9012, 괄호
'''
스택을 활용하여 '('를 만나면 1을 스택에 넣고, ')'를 만나면 이를 빼낸다
모든 문자를 스캔했을 때 1이 남아있거나, 중간에 스택이 비어있는데 pop하려고 한다면 이는 VPS가 아니다.
'''
import sys
input = sys.stdin.readline

n = int(input().rstrip())

result = []
for _ in range(n):
    stack_arr = []
    is_vps = True

    # 각 문자를 하나의 원소로 하는 리스트
    data = list(input().rstrip())
    for ch in data:
        if ch == '(':
            stack_arr.append(ch)
        else:
            if not stack_arr:
                # pop을 해야하는데 비어있다면, VPS가 아님
                is_vps = False
                break
            stack_arr.pop()

    if stack_arr:
        # 다 끝났는데 스택이 비어있지 않다면, VPS가 아님
        is_vps = False

    if is_vps:
        result.append("YES")
    else:
        result.append("NO")

# 출력
for res in result:
    print(res)

# 10:40