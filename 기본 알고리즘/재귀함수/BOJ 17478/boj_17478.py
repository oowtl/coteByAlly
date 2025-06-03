import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""


def bot(n: int):
    global N

    # _ 만들어주기
    before = "____" * n

    # base case
    if n > N-1:
        print(before + '"재귀함수가 뭔가요?"')
        print(before + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(before + '라고 답변하였지.')
        return

    # recursive case

    # 처음에만 하는 경우
    if n == 0:
        print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')

    print(before + '"재귀함수가 뭔가요?"')
    print(before + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print(before + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print(before + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')

    # 재귀 시작하는 부분
    bot(n + 1)

    print(before + "라고 답변하였지.")

N = int(input())
bot(0)
