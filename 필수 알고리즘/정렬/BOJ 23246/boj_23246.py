import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

"""
점수 계산식
리드 1
스피드 5
볼더링 2
10점

공식
1. 곱한 점수가 낮은 선수
2. 동일 점수 일 때는 합산 점수가 낮은 선수
3. 합산 점수 같으면 등 번호가 낮음 낮은 선수
"""

N = int(input())

score = [tuple(map(int, input().split())) for _ in range(N)]

# 전부 역순이라서 그대로 출력
leaderboard = sorted(score, key= lambda x : (x[1] * x[2] * x[3], sum(x[1:]), x[0]))

print(leaderboard[0][0], leaderboard[1][0], leaderboard[2][0])