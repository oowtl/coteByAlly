import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

# 조합에 대한 내장 라이브러리 잭ㅎㅇ
from itertools import combinations

LOTTO = 6

while True:
    I = list(map(int, input().split()))
    k = I[0]
    s = I[1:]

    if k == 0:
        break

    for comb in combinations(s, LOTTO):
        for u in comb:
            print(u, end = ' ')
        print()
    print()
