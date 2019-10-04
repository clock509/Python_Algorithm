#문제 5-1. 피보나치 수열을 만드시오.
#피보나치 수열: 0과 1부터 시작해서 바로 앞의 두 수를 더한 값을 다음 값으로 추가하는 방식으로 만든 수열.
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
#n번째 항 값 = n-1번째 항 값 + n-2번째 항 값


def fibonacci(n):
    if n <= 1:
        return n
    
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
