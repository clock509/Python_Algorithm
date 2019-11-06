#정렬(sort): 자료의 크기를 순서대로 맞춰 일렬로 나열하는 것.
#정렬 문제를 푸는 방법은 수없이 다양하고, 각 방법은 계산 복잡도나 특징이 달라 집중적으로 공부해야 할 필요가 있지만, 여기서는 대표적인 정렬 알고리즘 5가지를 정리하겠음.
#1. 선택 정렬(Selection sort)
#2. 삽입 정렬(Insertion sort)
#3. 병합 정렬(Merge sort)
#4. 퀵 정렬(Quicksort)
#5. 거품 정렬(Bubble sort)
############################################################################################################################################################
#선택 정렬이란?        작은 수부터 큰 수까지 크기 순으로 정렬하는 방법.
#쉽게 설명한 선택 정렬 알고리즘
#입력: 리스트 a
#출력: 정렬된 새 리스트
#주어진 리스트에서 최솟값의 위치를 돌려주는 함수
def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a):
    result = []  #새 리스트를 만들어 정렬된 값을 저장
    while a:     #주어진 리스트에 값이 남아있는 동안 계속
        min_idx = find_min_idx(a) #리스트에 남아있는 값 중 최솟값의 위치
        value = a.pop(min_idx)    #찾은 최솟값을 뺴내어 value에 저장
        result.append(value)
    return result

d = [2, 4, 5, 1, 3]
print(sel_sort(d))