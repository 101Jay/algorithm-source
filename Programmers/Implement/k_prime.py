# Programmers 92335, k진수에서 소수 개수 구하기
from collections import deque
from math import sqrt

def solution(n, k):
    answer = 0

    # 1. K진법으로 변환
    k_arr = deque([])
    while n // k != 0:
        remainder = n % k
        n = n // k
        k_arr.appendleft(str(remainder))
    k_arr.appendleft(str(n))

    k_num = "".join(list(k_arr))

    # 2. 0을 기준으로 나누기
    zero_split = k_num.split("0")

    # 3. 각각 소수인지 아닌지 파악
    for num in zero_split:
        if num != "" and is_prime(int(num)):
            answer += 1

    return answer


def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(sqrt(n)) + 1):  # 버림을 위한 int 함수 사용
        if n % i == 0:
            return False
    return True