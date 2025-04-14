import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

LOTTO_LEVEL = 6
case = []

def lotto(index, level):
    global K, S, case, LOTTO_LEVEL

    # Base Case
    if level == LOTTO_LEVEL:
        for c in case:
            print(c, end= ' ')
        print()
        return

    for i in range(index, K):
        case.append(S[i])
        lotto(i + 1, level + 1)
        case.pop()

while True:
    numbers = list(map(int, sys.stdin.readline().strip().split()))

    if numbers[0] == 0:
        break

    K = numbers[0]
    S = numbers[1:]
    lotto(0, 0)
    print()
