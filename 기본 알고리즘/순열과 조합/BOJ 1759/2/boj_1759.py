import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""
from itertools import combinations

L, C = map(int, input().split())
arr = input().split()
vows = ['a', 'e', 'i', 'o', 'u']

def is_possible(word):
    global L, C, vows

    vow = 0
    for c in word:
        vow += (c in vows)

    con = L - vow

    return vow >= 1 and con >= 2

arr.sort()

# combinations 를 사용하는 것이 편해보인다.
for word in combinations(arr, L):
    if is_possible(word):
        print(''.join(word))
