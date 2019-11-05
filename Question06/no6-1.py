#재귀호출을 이용한 무한급수 도형 표현.

#1. 사각 나선을 그리는 프로그램
# import turtle as t

# def spiral(sp_len):
#     if sp_len <= 5:
#         return
#     t.forward(sp_len)
#     t.right(90)
#     spiral(sp_len-5)

# t.speed(0)
# spiral(400)
# t.hideturtle()
# t.done()


#2. 시에르핀스키의 삼각형을 그리는 프로그램
# import turtle as t

# def triangle(tri_len):
#     if tri_len <= 10:
#         for i in range(0, 3):
#             t.forward(tri_len)
#             t.left(120)
#         return

#     new_len = tri_len / 2
#     triangle(new_len)
#     t.forward(new_len)
#     triangle(new_len)
#     t.backward(new_len)
#     t.left(60)
#     t.forward(new_len)
#     t.right(60)
#     triangle(new_len)
#     t.left(60)
#     t.backward(new_len)
#     t.right(60)

# t.speed(0)
# triangle(160)
# t.hideturtle()
# t.done()


#3. 나무를 그리는 프로그램.
# import turtle as t

# def tree(br_len):
#     if br_len <= 5:
#         return
#     new_len = br_len * 0.7
#     t.forward(br_len)
#     t.right(20)
#     tree(new_len)
#     t.left(40)
#     tree(new_len)
#     t.right(20)
#     t.backward(br_len)

# t.speed(0)
# t.left(90)        #default가 시작점에서 우측으로 이동하는 것으로 되어있음. 따라서 가지가 위쪽으로 뻗게 하려면 왼쪽으로 90도 튼 상태에서 시작해야 함.
# tree(70)
# t.hideturtle()
# t.done()


#4. 눈꽃을 그리는 프로그램.
import turtle as t

def snow_line(snow_len):
    if snow_len <= 10:
        t.forward(snow_len)
        return
    new_len = snow_len / 3
    snow_line(new_len)
    t.left(60)
    snow_line(new_len)
    t.right(120)
    snow_line(new_len)
    t.left(60)
    snow_line(new_len)

t.speed(0)
snow_line(150)
t.right(120)
snow_line(150)
t.right(120)
snow_line(150)
t.hideturtle()
t.done()