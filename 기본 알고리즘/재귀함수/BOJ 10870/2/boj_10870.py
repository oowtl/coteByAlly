import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')

data = input()

def solution(i):
    return fibo(int(i))

def fibo(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    return fibo(n - 1) + fibo(n - 2)

print(solution(data))