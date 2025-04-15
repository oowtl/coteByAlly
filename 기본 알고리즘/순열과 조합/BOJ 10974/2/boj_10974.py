import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""
from itertools import permutations

N = int(input())

for permutation in permutations(range(1, N + 1), N):
    print(' '.join(map(str, permutation)))