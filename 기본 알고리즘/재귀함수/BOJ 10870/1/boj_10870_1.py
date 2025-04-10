import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')

data = input()

def solution(data):
    return fibo(int(data))

# 반복문으로 피보나치 구현하기
def fibo(n: int) -> int:
    # 배열의 값은 안나올 것 같은 값으로 초기화 한다.
    # 배열의 크기는 넉넉하게
    arr = [-1] * (n + 2)
    arr[0] = 0 # 초기 값
    arr[1] = 1 # 초기 값

    for i in range(2, n + 1): # n + 1 로 해야 n 까지 계산 한다.
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[n]

print(solution(data))
