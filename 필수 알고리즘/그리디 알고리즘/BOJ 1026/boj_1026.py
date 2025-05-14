import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

"""
시간 제한 2초

길이 N 배열 A, B
S = A[0]*B[0] + ... + A[N-1]*B[N-1]
S 의 최솟값 출력 프로그램
A를 재배열 하는 것으로 풀어라

제약조건
0 <= N <= 50
0 <= A[i] <= 100
0 <= B[i] <= 100

큰 수는 큰 수 끼리 곱해야 커진다.
최소값을 만들기 위해서는 큰수와 작은 수를 곱해야한다.

A 재배열은 상관없음
고려해야할 경우의 수는 2가지
1. A 최소 * B 최대
2. A 최대 * B 최소
=> 2가지 경우의 수는 같은 경우이다. (착각;;)
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

a_min = 0
a_max = 0

for i in range(N):
    a_min += A[i] * B[N-1-i]
    a_max += A[N-1-i] * B[i]

print(min(a_min, a_max))
