import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

"""
1. 순열을 이용
- 순열을 이용할 떄의 경우의 수 = N!
- 순열을 이용하면 중복된 순열을 가려내야함 (추가 처리 필요)
- 중복된 순열을 가리는 공식 = N! / (p! * q! * ... r!)
p, q, r 은 같은 숫자의 개수이다.

이 문제의 핵심은 순열을 사용했을 떄, 중복된 순열이 존재한다는 것을 아는 것이다.
 

"""
from itertools import permutations

# 팩토리얼 계산 함수
def fact(x):
    if x == 0:
        return 1
    return fact(x - 1) * x

S = input()
ans = 0

for perm in permutations(S):
    ok = True
    for i in range(0, len(S) - 1): # -1 을 해야 if 문 조건식에서 인덱스 에러가 발생하지 않음
        if perm[i] == perm[i + 1]: # i == 0 부터 i == 최대인덱스 - 1 이면 모든 경우를 다 고려할 수 있음
            ok = False
            break
    ans += ok

for i in range(ord('a'), ord('z') + 1): # ord() : str -> int
    ans //= fact(S.count(chr(i))) # chr() : int -> str

print(ans)
