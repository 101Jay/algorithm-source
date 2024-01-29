# 프로그래머스, 자물쇠와 열쇠(2020 카카오 공채)

# import copy
#
# def solution(key, lock):
#     key_len = len(key)
#     lock_len = len(lock)
#     for rotation_num in range(1, 5):
#
#         key = rotate_key(key, rotation_num)
#
#         iter_num = lock_len + (key_len - 1)
#         # 검사할 영역을 지정한 이중 for문
#         for i in range(1, iter_num + 1):
#             if i > lock_len:
#                 check_row_num = lock_len - (i - lock_len)
#             else:
#                 check_row_num = i
#
#             for j in range(1, iter_num + 1):
#                 if j > lock_len:
#                     check_col_num = lock_len - (j - lock_len)
#                 else:
#                     check_col_num = j
#
#                 comp_arr = copy.deepcopy(lock)
#
#                 # compare and allocate - 지정된 영역 안에서 검사 수행
#                 # 비교 과정에서 행이 안 맞음
#                 fix_row = key_len - check_row_num
#                 fix_col = key_len - check_col_num
#                 fix_comp_row = 0
#                 fix_comp_col = 0
#
#                 if i > key_len:
#                     fix_comp_row = key_len - check_row_num
#                     fix_row = 0
#
#                 if j > key_len:
#                     fix_comp_col = key_len - check_col_num
#                     fix_col = 0
#
#                 conflict = False
#                 print("=========================")
#                 print(i, j)
#                 for row_i in range(check_row_num):
#                     for col_i in range(check_col_num):
#                         print("compare key :", row_i + fix_row, col_i + fix_col, "vs lock :", row_i + fix_comp_row,
#                               col_i + fix_comp_col)
#                         if key[row_i + fix_row][col_i + fix_col] == 1 and comp_arr[row_i + fix_comp_row][
#                             col_i + fix_comp_col] == 1:
#                             conflict = True
#                         if key[row_i + fix_row][col_i + fix_col] == 1 and comp_arr[row_i + fix_comp_row][
#                             col_i + fix_comp_col] == 0:
#                             comp_arr[row_i + fix_comp_row][col_i + fix_comp_col] = 1
#
#                 # check lock is opened
#                 # print(comp_arr)
#                 result = check_open(comp_arr)
#
#                 if result and conflict == False:
#                     return True
#
#     return False
#
#
# def check_open(lock):
#     lock_size = len(lock)
#     for i in range(lock_size):
#         for elm in lock[i]:
#             if elm == 0:
#                 return False
#
#     return True
#
#
# def rotate_key(key, r_num):
#     if r_num == 1:
#         return key
#
#     # 시계 방향 90도 회전
#     key_num = len(key)
#
#     new_key = copy.deepcopy(key)
#     for i in range(key_num):
#         for j in range(key_num):
#             # 해당 행 순회
#             new_key[j][key_num - (i + 1)] = key[i][j]
#
#     # print("new_key")
#     # print(new_key)
#     return new_key

###############################################
# 최종 답안
import copy

def solution(key, lock):
    key_len = len(key)
    lock_len = len(lock)
    for rotation_num in range(1, 5):

        key = rotate_key(key, rotation_num)

        iter_num = lock_len + key_len - 1
        # 검사할 행의 위치를 카운트
        for i in range(iter_num):

            # 검사할 열의 위치를 카운트
            for j in range(iter_num):

                # lock을 보존하면서 비교하기 위한 comp_lock
                comp_lock = copy.deepcopy(lock)

                # 돌기 간의 충돌을 체크하기 위한 변수 conflict
                conflict = False

                row_cnt = 0
                for k in range(key_len):
                    # i번만 비교하기 위한 장치
                    if row_cnt > i:
                        break
                    row_cnt += 1

                    lock_row = i - k
                    if lock_row < 0:
                        # 비교 불가능
                        continue
                    if lock_row >= lock_len:
                        # 비교 불가능
                        continue
                    key_row = key_len - 1 - k

                    col_cnt = 0
                    for h in range(key_len):
                        # j번만 비교하기 위한 장치
                        if col_cnt > j:
                            break
                        col_cnt += 1

                        lock_col = j - h
                        if lock_col < 0:
                            # 비교 불가능
                            continue
                        if lock_col >= lock_len:
                            # 비교 불가능
                            continue
                        key_col = key_len - 1 - h

                        # key와 lock의 비교
                        if key[key_row][key_col] == 1 and comp_lock[lock_row][lock_col] == 1:
                            conflict = True
                        if key[key_row][key_col] == 1 and comp_lock[lock_row][lock_col] == 0:
                            comp_lock[lock_row][lock_col] = 1

                # 자물쇠가 열렸는지 체크
                result = check_open(comp_lock)

                if result and conflict == False:
                    return True

    return False

def check_open(lock):
    lock_size = len(lock)
    for i in range(lock_size):
        for elm in lock[i]:
            if elm == 0:
                return False

    return True


def rotate_key(key, r_num):
    if r_num == 1:
        return key

    # 시계 방향 90도 회전
    key_num = len(key)

    new_key = copy.deepcopy(key)
    for i in range(key_num):
        for j in range(key_num):
            # 해당 행 순회
            new_key[j][key_num - (i + 1)] = key[i][j]

    return new_key