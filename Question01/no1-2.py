#문제 1. 1부터 n까지의 합 구하기
#풀이②

def calculator(n):
    s = n*(n+1) // 2    # //n : n으로 나눈 정수해
    return s

print(calculator(10))
print(calculator(100))






#풀이법: n(n+1)/2