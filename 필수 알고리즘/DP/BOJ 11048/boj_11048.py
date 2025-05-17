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

풀이
1. 전부 순회하는 경우에는 3^1000의 시간복잡도를 가진다.
2. 그리디한 풀이는 최적해가 아니다.
3. DP 로 가능

재귀 구조가 눈에 보인다. 재귀를 사용해서 풀 수 있을 것 같다.
주의할 점은 N,M 을 넘어가는 것을 막는 것, 각 방마다 가능한 최대 개수를 갱신하면서 가는 것 정도가 될 것 같다.

배열[0][0] 에 있는 것을 참조한다.
재귀 호출간에 상태를 저장하고 싶은데...? => 배열? 

점화식 f(0, 0) => max(f(x+1, y), f(x, y+1), f(x+1, y+1)) + arr[0][0]
이 점화식은 잘못된 것이다. 왜냐하면 식 작체가 성립하지 않기 때문 
나는 0,0 에서 x,y 까지 가는 것을 생각해서 이렇게 작성한 것이다. 근데 식이 성립하지 않는다.
f(x,y) = 점화식 으로 작성해야 식이 성립한다는 의미

---
점화식
f(r, c) = max(f(r-1, c), f(r, c-1), f(r-1, c-1)) + arr[r][c]
초기값 설정


"""
import sys
sys.setrecursionlimit(int(1e6))

INF = int(1e12)

def func(n, k): # dp[n][k]를 반환
	global cost, dp

	# base case
	if dp[n][k] != -1:
		return dp[n][k]

	# recursive case
	best = INF
	for i in range(3):
		if i != k:
			best = min(best, func(n - 1, i))

	dp[n][k] = best + cost[n][k]
	return dp[n][k]


N = int(input())
cost = [[0, 0, 0]]
cost += [list(map(int, input().split())) for _ in range(N)]

dp = [[0, 0, 0]] + [[-1, -1, -1] for _ in range(N)]

print(min(func(N, 0), func(N, 1), func(N, 2)))


