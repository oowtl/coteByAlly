import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), encoding='utf-8')
"""
=== input.txt 를 불러오기 위한 코드 ===
"""

# 문장 개수 입력
T = int(sys.stdin.readline().strip())
# 반복
for _ in range(0, T):
    # 문장 입력
    sentence = sys.stdin.readline().strip()
    reversed_sentence = sentence[::-1]
    # 역순인 문장과 비교
    if sentence == reversed_sentence:
        # 비교 횟수는 길이의 절반
        print(f"1 {len(sentence) // 2 + 1}")
    else:
        # 비교하다가 일치하지 않는 부분의 인덱스 반환
        for i in range(len(sentence) // 2):
            if sentence[i] != reversed_sentence[i]:
                print(f"0 {i + 1}")
                break
