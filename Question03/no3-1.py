#문제 3-1. n명 중 두 명을 뽑아 짝을 짓는다고 할 때, 짝을 지을 수 있는 모든 조합을 출력하는 알고리즘을 만들어 보라.
#ex) ["Tom", "Jerry", "Mike"]라면 Tom - Jerry, Tom - Mike, Jerry - Mike의 3가지 경우를 출력한다.

def pairs_name(x):
    n = len(x)
    for i in range(0, n-1):
        for j in range(i+1, n):
                print(x[i]+"_"+x[j])


a = ['Tom', 'Mike', 'Jane', 'Kain', 'David1', 'David2', 'Joseph']
print(pairs_name(a))