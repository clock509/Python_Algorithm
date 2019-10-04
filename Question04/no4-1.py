#문제 4-1. 1부터 n까지의 합을 재귀호출로 만드시오.

def sigma(n):
    if n == 0:
        return 0
    return n + sigma(n-1)

print(sigma(1))
print(sigma(10))