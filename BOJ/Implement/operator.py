# BOJ 14888, 연산자 끼워넣기
import sys
from itertools import permutations
INF = int(1e9)
N_INF = int(1e9) * -1
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

oper = list(map(int, input().rstrip().split()))
# 순서에 맞게 연산자 입력
oper_lst = ["+"] * oper[0] + ["-"] * oper[1] + ["*"] * oper[2] + ["//"] * oper[3]

# 모든 연산자로 가능한 순열을 구한 뒤, 동일한 순서쌍은 제거
oper_per = list(set(list(permutations(oper_lst, n-1))))

max_val, min_val = N_INF, INF

# 모든 연산자 조합을 순회하며 계산
for opers in oper_per:
    i = 0
    res = arr[i]
    i += 1

    for op in opers:
        t1 = res
        t2 = arr[i] # 다음 숫자 불러옴

        # 음수 // 양수라면 따로 처리해줘야 함
        if op == "//" and t1 < 0 and t2 > 0:
            res = ((t1 * -1) // t2) * -1
            i += 1
            continue

        # 그렇지 않다면, eval 함수 사용
        res = eval(str(t1) + op + str(t2))

        # i 업데이트
        i += 1

    # 결과값이 최댓값, 최솟값인지 경신
    if res < min_val:
        min_val = res

    if res > max_val:
        max_val = res

print(max_val)
print(min_val)