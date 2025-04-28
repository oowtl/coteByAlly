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

    print("{} {}".format(s_coord[i][0], s_coord[i][1]))