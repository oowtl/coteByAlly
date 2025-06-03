import sys
import os
from pprint import pprint
import math

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

"""
처음 시작하는 숫자가 0, 0 에서 그리는 것
이후에는 3,3 을 더하기 해서 사용한다.

"""

"""
N 부터 1 까지 감소하도록 설계
"""
def solution(n):
    global arr, L, base, center

    # base case
    if n == 1:
        arr[center][center] = '*'
        return

    # recursive case

    # center 에서 떨어진 만큼 가는 것
    # n = 1, 0 만큼
    # n = 2, 2 만큼
    # n = 3, 4 만큼

    # 시작점이 0,0 에서 2만큼 더 커짐
    # 길이가 5씩 줄어듬

    for i in range(0, L):
        for j in range(0, L):
            # 범위가 넘어가면 안됨
            if (base <= i <= L - 1 - base) and (base <= j <= L - 1 - base):
                # 네모 그리기
                if i == base or j == base or i == L - 1 - base or j == L - 1 - base:
                    arr[i][j] = '*'

    # 사각형을 그리기 시작하는 지점
    base += 2
    solution(n - 1)

N = int(input())

base = 0 # 사각형 그리기 시작지점
L = (N - 1) * 4 + 1 # 사각형의 길이
center = L // 2 # 전체 사각형의 중심
arr = [[' ' for _ in range(L)] for _ in range(L)]

solution(N)

for i in range(len(arr)):
    print("".join(arr[i]))