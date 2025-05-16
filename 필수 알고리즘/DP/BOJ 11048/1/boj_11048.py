import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

"""
제약 조건
1 <= N, M <= 1000
0 <= 사탕의 개수 <= 100

문제 요약
(1, 1) 에서 시작해서 (N, M)으로 끝남

이동할 수 있는 방법 3가지
1. (x+1, y)
2. (x, y+1)
3. (x+1, y+1)

각 방에는 사탕이 있고 이동할 때 가져올 수 있는 사탕의 최대값을 구한다.

"""
N, M = map(int, input().split())

arr = [[0] + list(map(int, input().split())) for _ in range(N)]
arr = [[0] * (M + 1)] + arr

dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
dp[1][1] = arr[1][1]

# 초기값 세팅
for j in range(2, M + 1):
    dp[1][j] = arr[1][j] + dp[1][j - 1]

for i in range(2, N + 1):
    dp[i][1] = arr[i][1] + dp[i - 1][1]

# 순회하면서 dp 테이블 갱신
for i in range(2, N + 1):
    for j in range(2, M + 1):
        dp[i][j] = arr[i][j]
        dp[i][j] += max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

print(dp[N][M])

