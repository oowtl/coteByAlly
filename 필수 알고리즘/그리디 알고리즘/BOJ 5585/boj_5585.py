import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

M = int(input())

# 잔돈
spending = 1000 - M

# 500, 100, 50, 10, 5, 1
# 단위 간에 우선순위가 확실하다. = 2개 이상을 조합할 때 우선순위가 달라지지 않음.

c_500 = spending // 500
spending %= 500

c_100 = spending // 100
spending %= 100

c_50 = spending // 50
spending %= 50

c_10 = spending // 10
spending %= 10

c_5 = spending // 5
spending %= 5

c_1 = spending // 1

result = c_500 + c_100 + c_50 + c_10 + c_5 + c_1
print(result)