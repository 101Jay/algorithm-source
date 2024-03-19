# Programmers 12987, 숫자 게임
def solution(A, B):
    answer = 0

    sorted_a = sorted(A)
    sorted_b = sorted(B)

    while sorted_a:
        a_num = sorted_a.pop()
        b_num = sorted_b.pop()

        if b_num > a_num:
            answer += 1
        else:
            # b는 다시 집어 넣기
            sorted_b.append(b_num)

    return answer