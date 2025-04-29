import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

T = int(input())

coordinates = [list(map(int, input().split())) for _ in range(T)]
s_coord = sorted(coordinates)

for i in range(T):

    print(s_coord[i][0], s_coord[i][1])

"""
시간 복잡도 계산 디테일
- 문제를 보고 1억의 시간 복잡도가 나오면(시간 초과로 인한 실패 기준) 상수항이나 연산 횟수를 상세하게 계산해야 한다.
-> 상수항으로 인해서 시간 초과가 날 수도 있기 때문

"""