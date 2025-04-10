import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

"""
func(k) : 입력이 k 일 떄 답을 출력하는 함수

시간 복잡도
한번의 호출로 인해서 발생하는 복잡도

func(n)
func(n-1) print() func(n-1)

3 번의 연산이 발생한다. (print 메서드는 3^(n-1) 이지만 빅오 연산을 하기 때문에)
따라서 시간복잡도는 O(3**n) 이 된다.
"""

# data = input()

def solution(n):
    if n == 0:
        return '-'

    return solution(n-1) + (' ' * (3 ** (n-1))) + solution(n-1)

while True:
    try:
        n = int(input())
        print(solution(n))
    except:
        break