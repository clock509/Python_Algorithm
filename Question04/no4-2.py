#문제 4-2. n개의 숫자 중에서 최댓값 찾기를 재귀호출로 만드시오.

def maxvalue(x, n):               #리스트 x의 앞부분 n개 중 최대값을 구하는 재귀함수.
    if n <= 1:
        return x[0]

    maxval_1 = maxvalue(x, n-1)   #n-1개 중 최댓값을 구함.
    if x[n-1] <  maxval_1:        #n-1개 중 최댓값과 n-1번 위치 값을 비교. 
        return  maxval_1
    else:
        return x[n-1]

a = [81, 22, 31, 654, 55]
print(maxvalue(a, len(a)))



#종료 조건: 자료값이 1개이면 그 값이 최대값
#재귀 호출 조건: n개 자료 중 최댓값 -> n-1개 자료 중 최댓값과 n-1번 위치값 중 더 큰 값.