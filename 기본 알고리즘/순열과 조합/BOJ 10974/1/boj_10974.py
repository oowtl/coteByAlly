import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""
def solution(level):
    global checked, choose, lst, T
    if level == T:
        print(*choose)
        return

    for i in range(T):
        if checked[i]:
            continue

        choose.append(lst[i])
        checked[i] = True
        solution(level + 1)
        checked[i] = False
        choose.pop()

T = int(input())
lst = [i for i in range(1, T + 1)]
checked = [False] * T
choose = []
solution(0)
