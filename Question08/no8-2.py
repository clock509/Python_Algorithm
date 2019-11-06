#내림차순 선택 정렬 프로그램 만들기.
#example(1), (2)에서 본 선택 정렬은 모두 오름차순이었음. 내림차순으로 바꾸려면, 아래 코드를 어떻게 바꾸어야 할까?

# #오름차순 선택 정렬
# def sel_sort(a):
#     n = len(a)
#     for i in range(0, n-1):
#         min_idx = i
#         for j in range(i+1, n):
#             if a[j] < a[min_idx]:
#                 min_idx = j
#         a[i], a[min_idx] = a[min_idx], a[i]
#         #print(a) #중간과정 출력

# d = [2, 4, 5, 1, 3]
# sel_sort(d)
# print(d)


#내림차순 선택 정렬
def sel_sort(a):
    n = len(a)
    for i in range(0, n-1): #0~n-2까지 반복
        #i번 위치부터 끝까지 자료 값 중 최댓값의 위치를 찾음
        max_idx = i
        for j in range(i+1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        #찾은 최댓값을 i번 위치로
        a[i], a[max_idx] = a[max_idx], a[i]
        #print(a) #중간과정 출력

d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d)