#팩토리얼: 1부터 n까지의 곱.
# n! = 1 x 2 x 3 x ... x (n-1) x n
#연속한 숫자의 곱을 구하는 알고리즘
#입력: n
#출력: 1부터 n까지 연속한 숫자를 곱한 값

def fact(n):
    f = 1                   #곱을 계산할 변수. 초기값 1.
    for i in range(1, n+1): #1부터 n까지 반복. (n+1)은 제외.
        f = f * i           #곱셉 연산으로 수정.
    return f

print(fact(1))
print(fact(5))
print(fact(7))