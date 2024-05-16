# SW Expert Academy 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기
T = int(input().rstrip())

answers = []

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input().rstrip())

    # 배열 선언
    arr = [0] * 101

    data_arr = list(map(int, input().rstrip().split()))

    # 1000개의 점수의 빈도 저장
    for data in data_arr:
        arr[data] += 1

    # 0~100점 중 빈도 수가 가장 높은 값 찾기
    max_score = 0
    max_val = 0

    for i in range(101):
        if arr[i] >= max_val:
            max_score = i
            max_val = arr[i]

    # 정답 저장
    answers.append(max_score)

# 정답 출력
for i, ans in enumerate(answers):
    print("#" + str(i + 1), ans)