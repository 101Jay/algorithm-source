# SW Expert Academy 1244. [S/W 문제해결 응용] 2일차 - 최대 상금
T = int(input().rstrip())
answer = []
for _ in range(T):
    num, change = map(int, input().rstrip().split())
    num_lst = list(str(num))
    max_num_lst = sorted(num_lst, reverse=True)
    size = len(num_lst)
    ans = num # 초기값 설정

    while change > 0:
        # num_lst의 각 원소를 자릿수 순서로 max_num_lst의 원소와 비교하며 바꿔줌
        for i in range(size):
            if num_lst[i] != max_num_lst[i]:
                tg = max_num_lst[i]
                tg_idx = 0
                tg_cnt = num_lst[i:].count(tg)

                # tg가 여러개 있을 때, 몇 번째 것을 가져올지 체크하는 변수 skip_num
                skip_num = 0
                if change >= tg_cnt:
                    skip_num = 0
                else:
                    skip_num = change - 1

                # 위치를 바꿀 숫자를 뒤에서부터 찾음
                for j in range(size-1, -1, -1):
                    if num_lst[j] == tg:
                        if skip_num == 0:
                            tg_idx = j
                            break
                        skip_num -= 1

                # 숫자 교환 수행
                num_lst[i], num_lst[tg_idx] = tg, num_lst[i]
                change -= 1
                break
        else:
            # for문이 모두 실행되었다면 더이상 교환할 것이 없는 것
            # 남은 change가 2로 나누어지지 않는다면 추가 교환이 필요할 수 있음
            if change % 2 != 0:
                # 중복되는 숫자가 있는지 확인 -> 그렇다면 이 둘을 바꿈으로써 숫자를 줄이지 않아도 됨
                for k in num_lst:
                    if num_lst.count(k) > 1:
                        break
                # 중복되는 숫자가 없다면 그렇지 않다면 일의 자리와 십의 자리를 바꿔줌
                else:
                    num_lst[size-1], num_lst[size-2] = num_lst[size-2], num_lst[size-1]

            ans = int("".join(num_lst))
            break

        # change가 0이 되었다면 ans를 업데이트
        if change == 0:
            ans = int("".join(num_lst))

    answer.append(ans)

for idx, ans in enumerate(answer):
    print("#" + str(idx+1), ans)