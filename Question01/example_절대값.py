#절대값 구하기 알고리즘
import math


#방법 1: 부호 판단
def abs_sign(a):
    if a>= 0:
        return a
    else:
        return -a

#방법 2: 제곱 후 제곱근 씌우기
def abs_square(a):
    b = a**2
    return math.sqrt(b)  #sqrt는 소수점이 붙은 값을 반환한다.

print(abs_sign(5))
print(abs_sign(-3))
print()
print(abs_square(5))
print(abs_square(-3))