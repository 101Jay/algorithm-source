# BOJ 9465
import sys
input = sys.stdin.readline

# 테스트케이스 입력
test_num = int(input().rstrip())

answer = []
for _ in range(test_num):
    n = int(input().rstrip())

    # 스티커의 점수 정보를 이차원 배열로 입력 받음
    arr = []
    for _ in range(2):
        row_data = list(map(int, input().rstrip().split()))
        arr.append(row_data)

    # n이 1일 때와 2일 때는 초기값 설정 없이 바로 정답 저장
    if n == 1:
        answer.append(max(arr[0][0], arr[1][0]))
        continue
    elif n == 2:
        answer.append(max(arr[0][0] + arr[1][1], arr[0][1] + arr[1][0]))
        continue

    # 점화식 사용을 위한 이차원 배열 초기화
    res = []
    for _ in range(2):
        row = [0] * n
        res.append(row)

    # 1, 2번째 위치 초기화
    res[0][0] = arr[0][0]
    res[1][0] = arr[1][0]
    res[0][1] = arr[0][1] + arr[1][0]
    res[1][1] = arr[0][0] + arr[1][1]

    # 점화식 구현
    for i in range(2, n):
        res[0][i] = max(res[1][i-1], res[1][i-2]) + arr[0][i]
        res[1][i] = max(res[0][i-1], res[0][i-2]) + arr[1][i]

    # 둘 중 더 큰 것을 선택
    answer.append(max(res[0][n-1], res[1][n-1]))

# 출력 형식에 맞게 정답 출력
for ele in answer:
    print(ele)