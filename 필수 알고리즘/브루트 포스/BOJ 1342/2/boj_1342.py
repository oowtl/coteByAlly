import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

"""
#2. 각 자리에 문자가 들어간다.
=> 자리 마다 무엇이 들어가야 하는지 판단해서 넣어준다.
=> 재귀 함수

## 풀이 아이디어
- 각 문자들의 개수를 저장하고 있다가 문자를 채워넣을 때 하나씩 줄인다.

핵심 아이디어 : 각 자리마다 철자가 들어간다.
- 각 자리마다 넣는 방법 : 재귀
- 철자를 모두 사용해야 하는 조건 : Map(Dict) - Key, Value
"""

def func(lev):
    global S, chars, cnt, choose, ans

    # base case
    if lev == len(S):
        ans += 1
        return

    # recursive case
    for c in chars:
        if cnt[c] == 0:
            continue

        # 백트래킹 : 답이 될 수 없는 것은 미리 패스하는 방법
        if (not choose) or (choose[-1] != c):
            cnt[c] -= 1
            choose.append(c)
            func(lev + 1)
            cnt[c] += 1
            choose.pop()

S = input()
chars = set() # 문자의 종류
cnt = dict()

# 입력값 넣어주기
for c in S:
    chars.add(c)
    # c 가 cnt의 키에 없는 경우 처리
    if c not in cnt:
        cnt[c] = 0
    cnt[c] += 1

choose = []
ans = 0

func(0)

print(ans)
