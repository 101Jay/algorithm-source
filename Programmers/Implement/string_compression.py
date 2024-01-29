# 프로그래머스, 문자열 압축 (2020 카카오 공채)

def solution(s):
    answer = 1000  # 최댓값으로 설정
    max_len = len(s) // 2
    s_len = len(s)

    # 길이가 1일 때의 예외처리
    if (s_len == 1):
        return 1

    for i in range(1, max_len + 1):
        result = ""
        k = 0
        target = ""
        short_cnt = 0
        while (k + i <= s_len):
            # print(target, short_cnt, k, i)
            if s[k:k + i] == target or target == "":
                # 압축이 가능할 때
                short_cnt += 1
            else:
                # 불가능할 때
                if short_cnt > 1:
                    result += str(short_cnt)
                result += target
                short_cnt = 1

            target = s[k:k + i]
            k = k + i

        # result에 반영되지 않은 것들 추가
        if short_cnt > 1:
            result += str(short_cnt)
        result += target
        result += s[k:s_len]

        # result의 길이가 최소인지 비교
        if answer > len(result):
            answer = len(result)

    return answer