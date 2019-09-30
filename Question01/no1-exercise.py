#1-1. 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 프로그램을 for문을 이용해 만들어 보기(ex. n = 3 -> 1^2 + 2^2 + 3^3)

def square_sum(n):
    s = 0
    for i in range(1, n+1):
        s += i**2
    return s

print(square_sum(10))

#1-3. n(n+1)(2n+1)/6 공식을 구현하라.
def square_sum2(n):
    s = n * (n+1) * (2*n + 1) // 6
    return s

print(square_sum2(10))