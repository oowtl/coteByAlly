import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

# data = int(input())
data = 5

# 숫자를 받아서 배열로 만들기 3^N
arr = [1] * (3 ** data)

def solution(arr):
    res = ""
    for i in range(0, len(arr)):
        if arr[i] == 0:
            res = res + " "
        elif arr[i] == 1:
            res = res + "-"

    return res

def kanto(start, end):
    global arr
    # 종료 조건
    if start >= end:
        return 0

    # 단위
    unit = (end - start + 1) // 3

    center_start = start + unit
    center_end = start + (unit * 2) -1
    # 오른쪽
    right_start = start
    right_end = center_start - 1
    # 왼쪽
    left_start = center_end + 1
    left_end = end

    # 관계
    for i in range(center_start, center_end + 1):
        arr[i] = 0

    # 재귀 호출
    kanto(right_start, right_end)
    kanto(left_start, left_end)

kanto(0, len(arr)-1)
s = solution(arr)
print(s)
