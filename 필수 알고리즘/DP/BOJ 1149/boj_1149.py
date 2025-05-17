import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

"""
제약 사항
2 <= N <= 1000
시간 0.5초
비용 <= 1000

문제 요약
집 N개에 R, G, B 3개 중 하나를 칠해야한다.
인접한 집의 색깔과 다르게 칠해야 한다. => 이전 집의 색과 같지 않으면 된다.
모든 집에 색깔을 칠했을 때의 최소비용을 구하라.

1. 비용을 저장할 곳은 N 과 같은 길이를 가지는 선형 리스트
2. 

점화식을 어떻게 잡아야 할까?

0 1 2
0 1 2
0 1 2
0 1 2

f(i) = min(f(i-1) + f(i-2) + ... + f(1)) + RGB[i]
이전 집에서 선택한 색깔이 아닌 색 중에서 최소값을 선택한다.
1번에서 R 을 선택하면 2번에서는 G, B 중에 하나를 선택한다.

"""


"""
풀이
dp 테이블을 일차원 선형 리스트로 할 경우에는 RGB 를 무엇으로 선택했는지 알 수가 어려워서 점화식을 도출하기 어렵다
=> 2차원 리스트를 사용하면 이 문제를 해결할 수 있다.

총 비용의 최소값이기 때문에 min(dp[N]) 이 된다.

그렇다면 값이 결정되는 것은?
R G B 를 0 1 2 라고 한다면 점화식은? 이전에 무엇을 선택했냐에 따라서 현재 선택하는 것이 달라진다.

dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])


"""

N = int(input())
cost = [[0,0,0]]
cost += [list(map(int, input().split())) for _ in range(N)]

dp = [[-1 for _ in range(3)] for _ in range(N+1)]

# 초기값 처리
dp[1][0] = cost[1][0]
dp[1][1] = cost[1][1]
dp[1][2] = cost[1][2]

# 1번째는 셋팅을 했기 때문에 2번째 부터 순회
for i in range(2, N+1):
    # 각 위치별 점화식
    dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[N]))
