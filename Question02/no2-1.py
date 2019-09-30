#문제 2-1. 숫자 n개를 입력받아 최솟값을 구하는 프로그램 만들기.
def min_value(x):
    n = len(x)
    min_value = x[0]
    for i in range(1, n):
        if min_value > x[i]:
            min_value = x[i]
    return min_value

a = [10, 20, 30, 40, 50, 1, 2, 5, 0, -1]
print(min_value(a))