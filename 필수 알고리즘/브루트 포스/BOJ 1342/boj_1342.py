import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

"""

1. 행운의 문자열 판단하기
2. 문자열의 순서 바꾸기

문자열 최대 길이 10
- 문자열 판단하기 : N
- 문자열의 순서 바꾸기 : N! 
"""


# 문자열
S = input()
result = 0

from itertools import permutations

# 순서가 있는 string
for ordered_string in permutations(S):

    ordered_string_len = len(ordered_string)
    lucky = True

    # 단어 순회
    for i in range(ordered_string_len - 1):
        if ordered_string[i] == ordered_string[i + 1]:
            lucky = False
            break

    if lucky:
        result += 1

def fact(x):
    if x == 0:
        return 1

    return x * fact(x - 1)

for i in range(ord('a'), ord('z') + 1): # a-z 를 순회하기 위해서는 z + 1 을 해줘야 한다.
    result //= fact(S.count(chr(i)))

print(result)