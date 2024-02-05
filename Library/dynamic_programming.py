'''
피보나치 수열을 통해 살펴보는 DP의 개념
메모리 공간을 조금 더 할애하여 연산 속도를 줄이는 접근 방식
1. Top-Down 방식 (메모이제이션)
    - 큰 문제를 해결하는 과정에서 작은 문제를 호출하는 방식
    - 일반적으로 재귀함수를 통해 구현
2. Bottom-Up 방식
    - 작은 문제부터 차근 차근 답을 도출하는 방식
    - 반복문을 활용하여 구현
'''

arr = [0] * 100

def fibo_topdown(x):

    if x == 1 or x == 2:
        return 1

    if arr[x] != 0:
        return arr[x]

    arr[x] = fibo_topdown(x-1) + fibo_topdown(x-2)
    return arr[x]


def fibo_bottomup(x):
    # x >= 3이라고 가정

    arr[1] = 1
    arr[2] = 1

    for i in range(3, x+1):
        arr[i] = arr[i-1] + arr[i-2]

    return arr[x]

# print(fibo_topdown(99))
# print(fibo_bottomup(99))