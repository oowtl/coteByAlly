import sys
import os
from os import remove

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

"""
N : 순열의 최대값
순열은 정렬된다.
작을 수록 앞에 정렬 = 이건 순열을 만들 때 배열을 정렬해서 만들면 그대로 순회 가능

문제
1. k 번째 순열 구하기
2. 주어진 임의의 순열이 정렬된 순열에서 몇번째인지

풀이
1. 부르트 포스
O(n) = O(20!)

2. 그리디
??
3. DP
점화식?

N = 4
=> 4 * 3 * 2 * 1
1. 1 로 시작하는 순열 6개 (3*2) 
{1,2,3,4}, {1,2,4,3}, {1,3,2,4}, {1,3,4,2}, {1,4,2,3,}, {1,4,3,2}
2. 1, 2 로 시작하는 순열 2개
{1,2,3,4}, {1,2,4,3}
3. 1, 2, 3 으로 시작하는 순열 1개 

2로 시작하는 셋팅
{2,1,3,4}

첫번째 자리가 넘어가면?
- 1->2로 넘어갈 때, (N-1)! 개를 넘어간다.

가장 최소의 값과의 차이로 비교하면 된다?
arr = [1,2,3,4]

만약에 {2,1,4,3} 와 비교하면?
1.첫번째 자리를 비교한다.
    - min(arr) 과 첫번째 자리 2를 비교해서 그 차이만큼 순서에 추가해준다.
    - (2-1) * (N-1)! 만큼의 숫자를 순서에 추가한다.
    - arr 에서 사용한 숫자 2를 뺀다.
2. 두번째 자리를 비교한다.
    - min(arr) 과 두번째 자리 1를 비교해서 그 차이만큼 순서에 추가해준다.
    - 차이가 0이라서 넘어간다.
    - arr 에서 사용한 숫자 1을 뺀다. filter, pop 등
3. 세번째 자리를 비교한다.
    - 반복
    
끝까지 돌리고 도출된 숫자

===
풀이 - 해당 순서의 순열 계산하기

자리별로 숫자를 배치한다.
각 자리에서 선택할 수 있는 최소값의 차이만큼 순서가 정해진다.
순서 값을 나눈 몫에 따라서 arr 에서 선택한다.
입력값으로 받은 순서를 빼준다.
선택한 arr 값은 제외한다.


"""

N = int(input())
T, *tmp = map(int, input().split())

# N 요소 배열
arr = [i for i in range(1, N + 1)]

# 초기값
first_question = tmp[0] - 1 # 1번 문제
second_question = tmp # 2번 문제

# 결과값
perm_result = [] # 요소 정보
order_result = 1 # 순서 정보

# 해당 순서의 순열을 계산하는 메서드
def sol_perm(idx):
    global N, arr,first_question, perm_result

    # base case
    if idx == N-1:
        # 마지막 요소 추가
        perm_result.append(arr.pop())
        return

    # recursive case
    standard_value = 1 # 해당 자리에서 숫자가 변경될 때마다 증가해야하는 순서
    for i in range(1, N-idx):
        standard_value *= i

    diff = first_question // standard_value
    choice = arr[diff] # 계속 요소를 제거하면서 진행할거라서 인덱스로 사용할 수 있다.
    perm_result.append(choice) # 결과에 추가
    arr.remove(choice) # 숫자 배열에서 제거해준다.

    # 뛰어넘은 값을 고려
    first_question -= standard_value * diff

    sol_perm(idx+1)

# 순서를 계산하는 메서드 - target_element
def sol_order(idx):
    global N, arr, second_question, order_result

    # base case
    if idx == N-1:
        return

    # recursive case
    standard_element = min(arr) # 비교 요소
    diff = second_question[idx] - standard_element # 차이값

    # 팩토리얼로 더하기
    result = 1
    for i in range(1, N-idx):
        result *= i

    order_result += result * diff
    # 선택한 값 삭제
    arr.remove(second_question[idx])
    sol_order(idx+1)

if T == 1:
    sol_perm(0)
    print(" ".join(map(str, perm_result)))
elif T == 2:
    sol_order(0)
    print(order_result)