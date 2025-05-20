import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

# Bottom Up

N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [-1 for _ in range(N + 1)] # 원소의 수를 고려하여 N + 1

# 초기값 처리 - DP 에서 중요한 것은 초기값 처리이다.
dp[1] = 1

# DP Table 갱신
for n in range(2, N + 1): # dp[n] 에 대한 반복문
    best = 0 # 한 자리 시작할 때마다 초기화
    for i in range(1, n): # 1 ~ n-1 까지 반복
        if arr[n] > arr[i]:
            best = max(best, dp[i]) # 1 ~ n-1 까지 순회하면서 가장 큰 길이의 부분 수열을 찾는 과정
    dp[n] = best + 1 # 순회하면서 best 의 값을 갱신했으니 DP Table 에 값을 저장

print(max(dp[1:]))