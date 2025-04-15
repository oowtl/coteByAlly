
# 1 부터 5 중 에서 2개를 나열하는 경우

def arr_permutation():
    checked = [False for _ in range(6)]

    for i in range(1, 6):
        checked[i] = True # 체크

        # 체크를 하고 실행 해야 하는 부분
        for j in range(1, 6):
            if checked[j]:
                continue
            print(i, j, end = ' | ')
        print()

        checked[i] = False # 체크 풀기

# arr_permutation()


# 재귀로 순열 구하기
N = 10
R = 3
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
check = [False] * N # 원소 사용 여부를 체크
# check[k] 가 true 이면 인덱스가 k인 원소가 사용중임을 나타냄.
# check[k] 가 false 이면 인덱스가 k인 원소가 사용중이지 않음을 나타냄.
choose = [] # 나열한 원소를 보관

def recursion_permutation(level):
    """
    level 이 있어야 한다. => level 을 넘으면 반환
    check 를 할 수 있어야 한다. => 배열

    뭔가를 저장해야 해 - 선형 자료구조, 비선형 자료구조에 저장하는 거지? = 저장을 할 수 있는 방법이 생각보다 많지가 않다는 것?
    1. 선형 자료구조
    - Static 배열
    - Dynamic 배열
    - Linked List
    - Stack
    - Queue
    2. 비선형 자료구조
    - Tree
    - Heap
    :return:
    """

    if level == R:
        print(choose)

    for i in range(N):
        if check[i]:
            continue

        choose.append(lst[i])
        check[i] = True # 추가 했기 때문에 check 해준다.

        recursion_permutation(level + 1)

        check[i] = False # pop 할거라서 check 를 풀어준다.
        choose.pop()


recursion_permutation(0)

