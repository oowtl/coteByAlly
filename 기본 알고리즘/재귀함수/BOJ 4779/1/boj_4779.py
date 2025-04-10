import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

# bottom up 방식
# 가장 작은 함수를 구하고 그 다음 함수와의 관계를 찾으면 된다.
# N 과 N - 1 사이의 관계

# 메모이제이션
ans = ['' for _ in range(20)]
# 첫 값
ans[0] = '-'

# 0을 제외한 후에 순회
for i in range(1, 13):
    # 관계식
    ans[i] = ans[i - 1] + (' ' * (3 ** (i - 1))) + ans[i - 1] # 문자열을 처리하는 시간이 걸리기 때문에 3^N 의 시간복잡도를 가진다.

while True:
    try:
        N = int(input())
        print(ans[N])
    except:
        break

