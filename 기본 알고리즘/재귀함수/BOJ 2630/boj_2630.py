import sys
import os
from curses import start_color

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""


"""
정사각형이 되는 조건을 맞추는 문제

변의 길이가 N/2 씩 되면서 줄어드는 구조, 변의 길이가 1일 때 순회 중지
하나의 사각형이 4개의 사각형으로 실행된다.
4개의 사각형을 순회해야 히는데 어떻게 순회할 인덱스를 넘겨주지? (각각의 범위를 지정해야함)

cut(x, y) 로 해서 시작 지점을 받는 것도 괜찮을 것 같다. => 길이는 어떻게 받지?(길이를 받아야 하는 이유 = 중간값 계산)
=> cut(x, y, n) 으로 한다?

def cut(x, y, n):
    # 종료 조건
    1. 변의 길이가 1이다.
    2. 변의 길이가 n이고 x,y 에서 시작하는 정사각형이 모두 같은 색상으로 칠해져 있다.
    
    # 재귀 호출 조건
    3. 순회한 결과 색상이 다르다.
    cut(x, y, n/2)
    cut(x + n/2, y, n/2)
    cut(x, y + n/2, n/2)
    cut(x + n/2, y + n/2, n/2)
    
합의 값으로 비교하거나 아니면 순회하다가 호출하는 방법이 있다. => 순회하다가 arr[x][y] 값과 다르면 호출하는 것으로

"""

N = int(input()) # 한 변의 길이
arr = [list(map(int, input().split())) for _ in range(N)] # 배열

white = 0
blue = 0

def cut(x, y, n):
    global white, blue

    # base case = 자른 길이가 1인 경우 or 영역의 모든 색상이 일치하는 경우
    if n == 1:
        if arr[y][x] == 0:
            white += 1
        else:
            blue += 1
        # 종료 한다.
        return

    # 시작 색상
    start_color = arr[y][x]
    cutting_length = n // 2

    # recursive case
    for i in range(n):
        for j in range(n):
            # 시작 시점 색상과 다른 경우에 재귀 호출
            if start_color != arr[y + i][x + j]:
                cut(x, y, cutting_length)
                cut(x + cutting_length, y, cutting_length)
                cut(x, y + cutting_length, cutting_length)
                cut(x + cutting_length, y + cutting_length, cutting_length)
                # 종료 해줘야 한다.
                return

    # 전부 일치하기 때문에 색종이 추가
    if start_color == 0:
        white += 1
    else :
        blue += 1

cut(0, 0, N)
print(white)
print(blue)