import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

"""
k 번째 숫자는 무엇인가?

흐름
1 시작 : 0
2 다름 : 01
3 같음 : 01 10
4 다름 : 0110 1001
5 같음 : 0110 1001 1001 0110
6 다름 : 0110 1001 1001 0110 1001 0110 0110 1001

1  : 0
2  : 1
3  : 1
4  : 0
5  : 1
6  : 0
7  : 0
8  : 1

9  : 1
10 : 0
11 : 0
12 : 1
13 : 0
14 : 1
15 : 1
16 : 0

길이 => 2^(실행 횟수-1)
k <= 2^(x-1)
로그를 하는 방법도 있지만, 재귀 호출을 하면서 종료 조건을 주는 방법도 있다.
k 가 10^18 이면? 이건 단순히 순회로는 불가능하다. 일반적인 순회로도 불가능 => 브루트포스로는 불가능하다.
=> 어떤 규칙을 찾아서 점화식으로 만들어야 함

점화식
k 가 홀수이면 2로 나눈 숫자의 반올림한 순서 숫자는 같다.
k 가 짝수이면 2로 나눈 숫자는 반대이다.

def check_string(문자열의 인덱스 n):
    # base case
    1. n == 1 return 0
    2. n == 2 return 1
    3. n == 3 return 1

    # recursive case
    1. n 이 짝수인지 확인 => 짝수이면 숫자 바꾸기
    2. n 이 홀수이면 그대로
    
글자 1번째를 인덱스 1로 잡고 풀었다. 그런데 이렇게 하면 홀수 점화식이 무너지게 된다. f(1) = 0, f(3) = 1
그래서 인덱스를 0부터 시작하는 것으로 바꾸면 성립

짝수
make_sentence(0) = 0
make_sentence(2) = 1
make_sentence(4) = 1

홀수
make_sentence(1) = 1
make_sentence(3) = 0
make_sentence(5) = 0

"""

k = int(input())

def check_string(n):
    # base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # recursice case
    elif n % 2 == 0: # 짝수 : 반대
        return check_string(n // 2)
    return 1 - check_string(n // 2)


s = check_string(k - 1)
print(s)