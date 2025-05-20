import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

"""
M, N : 가로, 세로 길이 (8 <= N, M <= 50)
8*8 로 잘라서 가장 적게 칠해야하는 최소 개수

칠해야 하는 사각형의 숫자를 담을 테이블을 만든다.
거기에서 8*8의 합을 구하는 테이블을 만든다.
최소값 출력한다.

현재 칸의 색상이 B 이라면 그 칸의 위, 왼쪽칸은 W 여야 한다.

if board[i][j] != board[i-1][j] and board[i][j] != board[i][j-1] => 0
else = 1

이렇게 만들려면? board의 0번째 행, 열에 대해서 값을 먼저 계산해야한다.

"""
from pprint import pprint
# N : 세로, M : 가로
N, M = map(int, input().split())

board = [input() for _ in range(N)]

repair = [[0 for _ in range(M)] for _ in range(N)]

# 0번째 행 초기화
for i in range(1, M):
    if board[0][i -1] == board[0][i]:
        repair[0][i] = 1

# 0번째 열 초기화
for i in range(1, N):
    if board[i][0] == board[i-1][0]:
        repair[i][0] = 1

# 전체 값 갱신
for i in range(1, N-1):
    for j in range(1, M-1):
        if board[i][j] == board[i-1][j] or board[i][j] == board[i][j-1]:
            repair[i][j] = 1

print("repair")
pprint(repair)

dp = [[0 for _ in range(M)] for _ in range(N)]

# 합산
for i in range(0, N):
    for j in range(0, M):
        if j + 8 <= M:
            dp[i][j] = sum(repair[i][j:j+8])


print("dp")
pprint(dp)

r = [sum(dp[i]) for i in range(N)]
print(min(r))