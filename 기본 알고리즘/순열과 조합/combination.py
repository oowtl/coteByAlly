"""
조합
- 순서가 존재하지 않음

조합을 구현하는 방법
1. for 문 : for 문을 r개 만큼 사용해야해서 확장성이 떨어짐
2. 재귀 함수 : r을 인자로 받아서 처리할 수 있어서 확장성이 좋음

# 파이썬에서는 조합을 만들어주는 라이브러리를 지원한다.
from itertools import combinations

조합의 시간복잡도는 조합 공식을 통해서 근사값을 구한다.
"""

N = 9
R = 5

lst = [1,2,3,4,5,6,7,8,9]
choose = []

def combination(index, level):
    # Base Case
    if level == R:
        print(choose)
        return

    for i in range(index, N):
        choose.append(lst[i]) # 요소 추가
        combination(i + 1, level + 1) # 다음 원소가 들어가는 역할 - 기존의 원소가 중복될 필요가 없으니까 i + 1
        choose.pop()

combination(0, 0)