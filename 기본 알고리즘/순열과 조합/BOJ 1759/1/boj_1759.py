import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

L, C = map(int, input().split())
arr = input().split()
vows = ['a', 'e', 'i', 'o', 'u']
choose = []

def is_possible():
    global L, C, choose, arr, vows

    vow = 0
    for c in choose:
        vow += (c in vows)
    # 자음 개수 = 전체 개수 - 모음 개수
    con = L - vow

    return vow >= 1 and con >= 2

def combination(idx, lev):
    global L, C, choose, arr

    # base case
    if lev == L:
        if is_possible():
            print(''.join(choose))
        return

    # recursive case
    for i in range(idx, C):
        # 조합을 배열로 관리한다는 것이 인상적.
        choose.append(arr[i])
        # 다음 레벨로 이동 하기
        combination(i + 1, lev + 1)
        # 전역에 있는 choose 를 사용하기 때문에 빼줘야 한다.
        choose.pop()

arr.sort()
combination(0, 0)