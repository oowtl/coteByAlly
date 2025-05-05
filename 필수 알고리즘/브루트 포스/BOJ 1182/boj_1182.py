import sys
import os
from typing import Tuple

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

# 정수의 개수 20
# 20 ^ 3 = 400 * 20 = 8000

# N : 정수의 개수
# S : 합 S

N, S = map(int, input().split())

numbers = list(map(int, input().split()))

result = 0

from itertools import combinations

# 조합의 개수
for comb_len in range(1, N+1):
    entire_permutation = combinations(numbers, comb_len)

    # 부분 수열 순회
    for partial_permutation in entire_permutation:

        # 부분 수열의 합과 S 비교
        if sum(partial_permutation) == S:
            result += 1

print(result)