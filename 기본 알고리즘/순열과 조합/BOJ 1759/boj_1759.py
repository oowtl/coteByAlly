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
vows = ["a", "e", "i", "o", "u"]


# 모음 체크
def check(sentence: str):
    global vows, s_length

    vow = 0
    for s in sentence:
        if s in vows:
            vow += 1
    con = max_level - vow
    return vow >= 1 and con >= 2


def combination(index, acc):
    if max_level == len(acc) and check(acc):
        print(acc)

    for i in range(index, s_length):
        combination(i + 1, acc + arr[i])


combination(0, "")
