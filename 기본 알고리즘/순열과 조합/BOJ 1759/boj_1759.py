import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

# 암호 글자 길이, 주어진 글자 길이
L, C = map(int, input().split())
arr = input().split()

# 정렬
arr.sort()

max_level = L
s_length = C
c_arr = ["a", "e", "i", "o", "u"]

# 완료 조건 체크
def check(sentence: str):
    # 모음 개수
    m_cnt = 0
    # 자음 개수
    j_cnt = 0

    for s in sentence:
        if s in c_arr:
            m_cnt += 1
        else:
            j_cnt += 1

    if m_cnt >= 1 and j_cnt >= 2:
        return True
    else:
        return False

def combination(index, acc):
    if max_level <= len(acc) and check(acc):
        print(acc)
        return

    for i in range(index, s_length):
        combination(i + 1, acc + arr[i])

combination(0, "")
