#리스트에 찾는 값이 나오는 모든 위치를 리스트로 돌려주는 탐색 알고리즘 만들기(원래는 여러 개 있더라도 첫 번째 위치만 결과로 돌려줌).
#찾는 값이 리스트에 없다면 빈 리스트 반환.

def seq_search(x, y):
    empty = []
    loc = []
    n = len(x)
    for i in range(0, n):
        if y == x[i]:
            loc.append(i)
    return loc

    return empty


v1 = [10, 20, 20, 30, 50, 20]
print(seq_search(v1, 20))
print(seq_search(v1, 60))


#계산 복잡도: O(n)  #탐색하는 값이 중간에 나오더라도 탐색을 멈추지 않고 혹시 더 있을 자료 값을 찾기 위해 끝까지 탐색을 해야 하므로, 어느 경우이든 비교가 n번 필요. 