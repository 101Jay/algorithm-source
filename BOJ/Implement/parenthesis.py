# BOJ 2504, 괄호의 값
import sys
from collections import deque
sys.setrecursionlimit(1000)
input = sys.stdin.readline

data = list(input().rstrip())

def paren_eval(str_data):
    result = 0

    if not str_data:
        # 비어있다면 1을 반환
        return 1

    queue = deque(str_data)
    while queue:
        ch = queue.popleft()

        # ( 일 때
        if ch == "(":
            # 같은 레벨의 )가 나올 때까지 찾아야 함
            stack = ["("]
            temp = []
            while stack:
                ch = queue.popleft()
                if ch == ")":
                    # 무조건 올바른 것이라고 가정
                    stack.pop()

                if ch == "(":
                    stack.append("(")

                # 그렇지 않을 경우 temp에만 저장
                if stack: # stack이 비지 않을 때만 넣어줌으로써 괄호 안의 것들만 남김
                    temp.append(ch)

            result += 2 * paren_eval(temp) # 괄호 내부에 있는 것을 다시 재귀적으로 계산

        # [ 일 때
        if ch == "[":
            # 같은 레벨의 ]가 나올 때까지 찾아야 함
            stack = ["["]
            temp = []
            while stack:
                ch = queue.popleft()
                if ch == "]":
                    # 무조건 올바른 것이라고 가정
                    stack.pop()

                if ch == "[":
                    stack.append("[")

                # 그렇지 않을 경우 temp에만 저장
                if stack:  # stack이 비지 않을 때만 넣어줌으로써 괄호 안의 것들만 남김
                    temp.append(ch)

            result += 3 * paren_eval(temp)  # 괄호 내부에 있는 것을 다시 재귀적으로 계산

    return result

def paren_correct(str_data):
    queue = deque(str_data)
    stack = []

    while queue:
        ch = queue.popleft()
        if ch == "(":
            stack.append(ch)

        if ch == "[":
            stack.append(ch)

        if ch == ")":
            if not stack:
                return False

            temp = stack.pop()
            if temp != "(":
                return False

        if ch == "]":
            if not stack:
                return False

            temp = stack.pop()
            if temp != "[":
                return False

    # 스택이 모두 비어있어야 최종적으로 True
    if not stack:
        return True

    return False


# 올바른 괄호인지 확인
if not paren_correct(data):
    print(0)
else:
    print(paren_eval(data))