# 프로그래머스, 가사 검색
from bisect import bisect_left, bisect_right

def solution(words, queries):
    word_lst = [None] * 10000
    reverse_word_lst = [None] * 10000

    for word in words:
        size = len(word) - 1

        if word_lst[size] == None:
            reverse_word_lst[size] = []
            word_lst[size] = []

        word_lst[size].append(word)
        # 간결하게 문자열을 뒤집는 방식
        reverse_word_lst[size].append(word[::-1])

    for i in range(10000):
        if word_lst[i] == None:
            continue

        # query 탐색시마다 sorting 하는 것보다 한 번 다 해놓고 그냥 쓰는 것이 효율적
        word_lst[i].sort()
        reverse_word_lst[i].sort()

    answer = [0] * len(queries)

    for i, query in enumerate(queries):
        size = len(query)

        if query[-1] != '?':
            words = reverse_word_lst[size - 1]
            query = query[::-1]
        else:
            words = word_lst[size - 1]

        # 빈 배열이라면
        if words == None:
            continue

        # 이미 탐색 범위를 많이 좁혀놨음으로 바로 변경
        qu_first = query.replace('?', 'a')
        qu_last = query.replace('?', 'z')

        # 해당 구간 사이에 있는 단어들의 갯수를 구함
        result = bisect_right(words, qu_last) - bisect_left(words, qu_first)

        # 해당 위치에 계산 결과 저장
        answer[i] = result

    return answer

'''
1. 단어 길이 단위로 리스트를 분리하면서 (사전식) 정렬을 통해 이진탐색이 가능하도록 함
2. 접두사의 경우 비교 대상 단어들과 쿼리를 모두 뒤집음으로써 위와 같은 로직으로 이진탐색이 가능하도록 함
'''