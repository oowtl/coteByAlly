import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

# Top Down

def func(n):
    # dp n을 반환한다.
    global arr, dp, cal

    # base case
    if dp[n] != -1: # dp[n] 까지 갱신되었을 때, 재귀를 종료한다.
        return dp[n]

    # recursive case
    best = 0
    for i in range(1, n):
        if arr[n] > arr[i]:
            best = max(best, func(i))

    dp[n] = best + 1
    return best + 1

N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [-1 for _ in range(N + 1)] # 원소의 수를 고려하여 N + 1

# 초기값 처리 - DP 에서 중요한 것은 초기값 처리이다.
dp[1] = 1

# dp[1] ~ dp[N] 까지 구하기
for n in range(1, N+1):
    func(n)

print(max(dp[1:]))
