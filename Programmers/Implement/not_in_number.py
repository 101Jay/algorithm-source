# Programmers 86051, 없는 숫자 더하기
def solution(numbers):
    answer = -1

    comp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for num in numbers:
        comp.remove(num)

    answer = sum(comp)

    return answer