#최대값 구하기 알고리즘
#최대값이 있는 위치 번호를 돌려주는 알고리즘.
import math


def find_max(x):
    n = len(x)              #x의 크기를 n에 할당
    max_idx = 0             #리스트의 0번 위치를 최대값 위치로 지정.
    for i in range(1, n):   #1부터 n-1번까지 반복
        if x[i] > x[max_idx] :    #이번 값이 현재까지 기억된 최대값보다 크다면, 최대값의 위치를 변경.
            max_idx = i
    return max_idx            #최대값의 인덱스 반환.


a = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(a))