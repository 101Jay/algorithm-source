# BOJ 4673, 셀프 넘버
def make_d(n):
    size = len(str(n)) - 1 # 10의 몇 승인지 확인

    result = n
    while size >= 0:
        result += n // (10 ** size) # 자릿수 더하기
        n = n % (10 ** size) # n을 갱신
        size -= 1

    return result

# list를 활용하여 결과가 10000 이하인 것 저장
check_lst = [False] * 10001
for i in range(1, 10001):
    target = make_d(i)
    if target <= 10000:
        check_lst[target] = True

# False인 것들을 출력
for j in range(1, 10001):
    if not check_lst[j]:
        print(j)