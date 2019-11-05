#학생 번호와 이름이 리스트로 주어졌을 때, 학생 번호를 입력하면 학생 번호에 해당하는 이름을 순차 탐색으로 찾아 돌려주는 함수 만들기.
#해당하는 학생 번호가 없으면 물음표 출력.

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

def student_find(x, y):
    for i in range(0, len(x)):
        if y == x[i]:
            return stu_name[i]

    return "?"


print(student_find(stu_no, 14))
print(student_find(stu_no, 39))
print(student_find(stu_no, 50))