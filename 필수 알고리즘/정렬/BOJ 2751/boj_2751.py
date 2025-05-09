import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

"""
N 의 최대가 100만이다.
정렬을 하면 시간이 많이 걸리는데..?
그럼 어떻게 해야 시간이 적게 걸리는거지?

min, max?
배열을 나눠서?

의문인 것은 n log n 이 600만인데 왜 시간초과가 발생하는 것인지 모르겠다.

python3 로 할 때는 동작하지 않던 코드가 pypy3 에서는 동작함.
"""


N = int(input())
arr = sorted([int(input()) for x in range(N)])

for i in range(len(arr)):
    print(arr[i])