# 프로그래머스 60060, 가사 검색
from bisect import bisect_left, bisect_right

def search_query(query, words):

    '''
    ?패턴은 모두 문자 뒤쪽에 있는 상황
    ?가 아니면 모두 영어 소문자라는 특징을 활용하여, ?인 부분을 a로 모두 치환한 값과 z로 모두 치환한 값을 활용하여 탐색
    bisect_left는 해당 원소보다 크거나 같은 원소들이 모두 오른쪽에 갈 수 있도록 해당 원소를 배치
    bisect_right는 해당 원소보다 작거나 같은 원소들이 모두 왼쪽에 갈 수 있도록 해당 원소를 배치
    '''

    left_target = query.replace("?", "a")
    right_target = query.replace("?", "z")

    result = bisect_right(words, right_target) - bisect_left(words, left_target)

    return result

def solution(words, queries):
    answer = []

    # words를 각 단어들의 길이에 따라서 나눠서 저장
    words_by_len = [None] * 10001 # 최대 길이 10000
    reverse_words = [None] * 10001

    for target in words:
        size = len(target)

        if not words_by_len[size]:
            # None일 경우 리스트 생성
            words_by_len[size] = []
            reverse_words[size] = []

        words_by_len[size].append(target)
        reverse_words[size].append(target[::-1]) # slice를 활용하여 간편하게 뒤집기

    # 이진 탐색을 위해, 각 words_by_len의 원소들, 즉 그 안의 단어 리스트들을 정렬
    # 이진 탐색 과정에서 정렬할 경우 매번 정렬을 다시해야 함으로 한 번에 미리 해두는 것이 최악의 경우에 효율적
    for lst in words_by_len:
        if not lst:
            continue
        lst.sort()

    for rev in reverse_words:
        if not rev:
            continue
        rev.sort()

    # 각 쿼리마다 해당 쿼리 사이즈에 맞는 단어들의 리스트를 이진탐색으로 순회하며 키워드가 일치하는지 확인
    for query in queries:
        query_size = len(query)
        target_words = words_by_len[query_size]

        # target_words에 탐색을 위한 단어가 없다면, 해당 쿼리 자리에는 0을 추가
        if not target_words:
            answer.append(0)
            continue

        # query에서 ?가 앞부분에 나온다면 뒤집는 버전으로 함수 실행
        if query.find("?") == 0:
            match_num = search_query(query[::-1], reverse_words[query_size])
        else:
            match_num = search_query(query, target_words)

        answer.append(match_num)

    return answer


# 입출력 예시
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))