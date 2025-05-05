import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

def search(lev):
    global N, S, arr, cur_sum, ans

    # base case
    if lev == N:
        if cur_sum == S:
            ans += 1
        return

    # 인덱스가 lev인 원소 선택 O
    cur_sum += arr[lev]
    search(lev + 1)
    cur_sum -= arr[lev]

    # 인덱스가 lev인 원소 선택 X
    search(lev + 1)


N, S = map(int, input().split())
arr = list(map(int, input().split()))
cur_sum = 0
ans = 0

search(0)
if S == 0:
    ans -= 1

print(ans)