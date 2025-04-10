import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

data = int(input())

def solution(data):
    return fibo(data)

# 메모이제이션
arr = [-1] * (data + 2)
arr[0] = 0
arr[1] = 1


def fibo(n: int) -> int:
    global arr # 전역 변수 사용

    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[n]

print(solution(data))