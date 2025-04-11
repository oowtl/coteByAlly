import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

cnt = 0

def is_palindrome(s):
    global cnt
    return recursion(s, 0, len(s)-1)

test_case = int(input())
while True:
    try:
        cnt = 0
        sentence = input()
        print(f"{is_palindrome(sentence)} {cnt}")
    except:
        break