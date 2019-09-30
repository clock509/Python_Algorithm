#최대값 구하기 알고리즘
import math


def find_max(x):
    n = len(x)              #x의 크기를 n에 할당
    max_v = x[0]            #x의 0번째 값을 최대값으로 설정.
    for i in range(1, n):   #1부터 n-1번까지 반복
        if x[i] > max_v:    #이번 값이 최대값보다 크다면, 이번 값을 최대값으로 설정한다.
            max_v = x[i]
    return max_v            #최대값 반환


a = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(a))