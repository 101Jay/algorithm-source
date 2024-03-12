# Programmers 150365, 미로 탈출 명령어
def solution(n, m, x, y, r, c, k):
    answer = ''
    queue = []

    # r, c로 가는데 필요한 문자열 찾기
    if r - x > 0:
        for _ in range(r - x):
            queue.append('d')
    elif r - x < 0:
        for _ in range(x - r):
            queue.append('u')

    if c - y > 0:
        for _ in range(c - y):
            queue.append('r')
    elif c - y < 0:
        for _ in range(y - c):
            queue.append('l')

    # queue의 크기가 k보다 크거나, k에서 queue의 사이즈만큼 뺀 것이 2의 배수가 아니라면 출력 후 종료
    size = len(queue)
    if size > k or (k - size) % 2 != 0:
        return "impossible"

    # queue를 사전 역순으로 정렬
    queue.sort(reverse=True)

    template = ['d', 'l', 'r', 'u']
    step = [(1, 0), (0, -1), (0, 1), (-1, 0)]

    limit = 0
    while limit < k:
        limit += 1

        for i, elem in enumerate(template):

            # 경계선을 넘어가는지 체크
            mv_x, mv_y = x + step[i][0], y + step[i][1]
            if mv_x <= 0 or mv_x > n or mv_y <= 0 or mv_y > m:
                continue

            # 만약 이미 queue가 비었다면, 해당 문자와 반대 급부의 문자를 넣고 진행
            if not queue:
                queue.append(rev_dir(elem))
                queue.append(elem)

            # 해당 문자가 사용 가능하다면, 사용 후 이동
            if queue[-1] == elem:
                answer += queue.pop()
                x, y = mv_x, mv_y
                break
            # 해당 문자가 사용 불가하다면
            else:
                # k - (queue사이즈 + limit)가 2보다 크거나 같은지 확인
                if k - (len(queue) + limit - 1) >= 2:
                    # 해당 문자를 사용한 셈치고, 반대 급부를 사용할 queue에 추가
                    answer += elem
                    queue.append(rev_dir(elem))
                    # queue 재정렬
                    queue.sort(reverse=True)
                    x, y = mv_x, mv_y
                    break

                # 2보다 작다면, 더이상 추가할 수 없음으로 그냥 continue
                continue

    return answer

def rev_dir(elem):
    if elem == 'u':
        return 'd'
    elif elem == 'd':
        return 'u'
    elif elem == 'r':
        return 'l'
    else:
        return 'r'