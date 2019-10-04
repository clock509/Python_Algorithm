#유클리드가 발견한 최대공약수의 성질
#1) a와 b의 최대공약수는 'b'와 'a를 b로 나눈 나머지'의 최대공약수이다. 즉, gcd(a, b) = gcd(b, a%b)이다.
#2) 어떤 수와 0의 최대공약수는 자기 자신이다. 즉, gcd(n, 0) = n이다.

#예:
# gcd(60, 24) = gcd(24, 60 % 24) = gcd(24, 12) = gcd(12, 24 % 12) = gcd(12, 0) = 12
# gcd(81, 27) = gcd(27, 81 % 27) = gcd(27, 0) = 27
# '재귀 호출'로 풀어가는 것이 힌트!


#유클리드 방식을 이용해 최대공약수를 구하는 알고리즘.
def gcd(a, b):
    if b == 0:            #종료 조건
        return a
    return gcd(b, a % b)  #좀 더 작은 값으로 자기 자신을 호출

print(gcd(1, 5))
print(gcd(3, 6))
print(gcd(60, 24))
print(gcd(81, 27))