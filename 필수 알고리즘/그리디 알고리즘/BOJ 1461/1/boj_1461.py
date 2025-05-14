import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

"""
제약 조건
시간제한 : 2초
0 <= N, M <= 50
책의 위치 != 0
|책의 위치| <= |10000|

브루트 포스 : 책의 모든 순서 O(N!)

그리디 풀이

M권을 다 가져가는 것이 이득이다.
단, 방향을 바꿀 때는 고려하지 않는 것이 이득이다. 
먼곳을 먼저 가는 것이 이득이다.

구현
음수 좌표와 양수 좌표를 동시에 처리할 필요는 없다.
"""

N, M = map(int, input().split())
books = list(map(int, input().split()))

neg = []
pos = []

for x in books:
    if x > 0:
        pos.append(x)
    else:
        neg.append(-x)

pos = sorted(pos)[::-1]
neg = sorted(neg)[::-1]

# 먼 곳을 먼저하는 것이 좋을 것 같다고 생각한 것은 올바른 접근이었다.
# 다만 거리를 저장하는 배열을 만들어서 활용하는 것을 생각하지 못함
dists = []

# 슬라이싱을 통해서 이동할 거리를 가져옴
for p in pos[::M]:
    dists.append(p)

for n in neg[::M]:
    dists.append(n)

# 가장 큰 거리를 빼주는 것읆 생각하지 못함
print(2 * sum(dists) - max(dists))




