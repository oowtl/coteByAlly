import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

N = int(input())
stack = []
top = 0

for _ in range(N):
    x = input().split()

    if x[0] == 'push':
        stack.append(x[1])
        top += 1
    elif x[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            p = stack.pop()
            print(p)
            top -= 1
    elif x[0] == 'size':
        print(len(stack))
    elif x[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif x[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[top-1])

