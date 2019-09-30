#문제 1. 1부터 n까지의 합 구하기
#풀이①
def calculator(n):
    s = 0
    for i in range(1, n+1):
        s += i                #s = s+i
    return s

print(calculator(10))
print(calculator(100))



#풀이법:  1+2+3+...n
#풀이과정
#1. 합을 기록할 변수 s를 만들고 0을 저장한다.
#2. 변수 i를 만들어 1부터 n까지의 숫자를 1씩 증가시키며 반복함.
#3. [반복 블록] 기존의 s에 i를 더하여 얻은 값을 다시 s에 저장한다.
#4. 반복이 끝났을 때 s에 저장된 값이 결과값!