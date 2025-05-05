import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

"""
부분 수열

n1, n2, n3 로 3개의 숫자로 이루어진 수열이라면?
수열은 각 숫자를 선택하거나 선택하지 않거나의 모음

숫자 : 1, 2, 3
선택 : O, X, O
결과 수열 : (1, 3)

따라서 복잡도 계산은 있거나 없거나 2가지 경우로 계산한다.
- 부분 수열의 크기 : 2^N - 1 (공집합 제외)

그래서 재귀를 이용해서 문제를 풀 수 있다.
"""

def search(lev):
    global N, S, arr, choose, ans

    # base case
    if lev == N:
        if choose and sum(choose) == S:
            ans += 1
        return

    # 인덱스가 lev인 원소 선택 O
    choose.append(arr[lev])
    search(lev + 1)
    choose.pop()

    # 인덱스가 lev인 원소 선택 X
    search(lev + 1)


N, S = map(int, input().split())
arr = list(map(int, input().split()))
choose = []
ans = 0

search(0)

print(ans)