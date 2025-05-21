import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

"""
Bottom-UP
"""

s1 = input()
s2 = input()

N, M = len(s1), len(s2)
s1 = " " + s1
s2 = " " + s2

# 초기값 처리
dp = [[0] * (M + 1) for _ in range(N + 1)] # 첫 번째 행과 열을 0으로 처리하여 dp[n][m] = max(dp[n - 1][m], dp[n][m - 1]) 을 예외 처리 없이 실행할 수 있다.

# DP Table 갱신
for n in range(1, N + 1):
    for m in range(1, M + 1): # dp[n][m]
        if s1[n] == s2[m]: # 같을 때의 처리
            dp[n][m] = dp[n - 1][m - 1] + 1
        else:
            dp[n][m] = max(dp[n - 1][m], dp[n][m - 1]) # 같지 않다면 2차원 배열의 위쪽과 왼쪽의 요소를 참조한다.

print(dp[N][M])
