import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

"""
Top-Down
"""

import sys
sys.setrecursionlimit(int(1e6))

def func(n, m):
    # dp[n][m]을 반환
    global s1, s2, dp

    # base case
    if n == 0 or m == 0: # 초기값 처리 : 1행과 1열의 값을 0으로 초기화 한다.
        return 0

    if dp[n][m] != -1: # 초기값 처리가 되었거나 값이 구해진 자리는 바로 값을 반환한다.
        return dp[n][m]

    # recursive case
    if s1[n] == s2[m]:
        dp[n][m] = func(n - 1, m - 1) + 1
    else:
        dp[n][m] = max(func(n - 1, m), func(n, m - 1))

    return dp[n][m]


s1 = input()
s2 = input()

N, M = len(s1), len(s2)
s1 = " " + s1
s2 = " " + s2

dp = [[-1] * (M + 1) for _ in range(N + 1)]

print(func(N, M))
