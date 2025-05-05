
def search(lev):
    global arr, N, choose

    # base case
    if lev == N:
        print("END : ", lev, choose)
        return

    # 인덱스가 lev인 원소 선택 O
    choose.append(arr[lev])
    print("=== : ", lev,  choose)
    search(lev + 1)
    choose.pop()

    # 인덱스가 lev인 원소 선택 X
    search(lev + 1) # 여기에서는 append 없이 lev 만 상승하기 때문에 요소를 선택하지 않고 넘어가는 형태가 된다.

N = 4
arr = [i for i in range(N)]
choose = []
ans = 0

search(0)